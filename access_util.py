import sqlite3
import requests
import datetime
import sys
import toml

def getIPs():
    r = requests.get('https://www.cloudflare.com/ips-v4')
    return r.text.split("\n")


def findOldCloudflareIps(cur):
    old_ips = []
    cloudflare_list_id = None
    if (cloudflare_list_id := findListID(cur, "Cloudflare")):     
        for row in cur.execute(f"SELECT * FROM access_list_client WHERE access_list_id = {cloudflare_list_id}"):
            old_ips.append(row[4])
    return old_ips


def findListID(cur, name):
    for row in cur.execute("SELECT id,name FROM access_list"):
        if row[1] == name:
            return row[0]
    return None


def makeCloudflareList(cur):
    cloudflare_list_id = (findListID(cur, "Cloudflare") or None)
    if cloudflare_list_id:
        cur.execute(f"DELETE FROM access_list_client WHERE access_list_id = '{cloudflare_list_id}'")
    else:
        date_string = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        cur.execute(f"INSERT INTO access_list(created_on,modified_on,owner_user_id,name,meta) VALUES ('{date_string}','{date_string}',1,'Cloudflare,'{{}}')")
        cloudflare_list_id = cur.lastrowid
    return cloudflare_list_id


def insertIPs(cur, list_id, ips):
    date_string = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    for address_insert in ips:
        cur.execute(f"INSERT INTO access_list_client(created_on,modified_on,access_list_id,address,directive,meta) VALUES ('{date_string}','{date_string}',{list_id},'{address_insert}','allow','{{}}')")


"""Assumes the Cloudflare list exists even if not populated
"""
def getListsUsingCloudflare(cur):
    lists_to_update = []
    old_ips = findOldCloudflareIps(cur)
    if len(old_ips) != 0:
        for row in cur.execute("SELECT access_list_id FROM access_list_client WHERE address = ?", [old_ips[0]]):
            lists_to_update.append(row[0])
        lists_to_update = list(set(lists_to_update))
    else:
        lists_to_update = [findListID(cur, "Cloudflare")]
    return lists_to_update


def updateAllCloudflareIPs(cur):
    new_ips = getIPs()
    old_ips = findOldCloudflareIps(cur)
    if set(old_ips) != set(new_ips):
        lists_to_update = getListsUsingCloudflare(cur)
        
        for address_delete in old_ips:
            cur.execute(f"DELETE FROM access_list_client WHERE address = '{address_delete}'")
        
        for list_id in lists_to_update:
            insertIPs(cur, list_id, new_ips)
        return True
    return False


def removeCloudflare(cur, listID):
    IPs = findOldCloudflareIps(cur)
    for address_delete in IPs:
        cur.execute(f"DELETE FROM access_list_client WHERE address = '{address_delete}' AND access_list_id = {listID}")


def main():
    with open("config.toml", "r") as f:
        db_path = toml.load(f)["db_path"]

    con = sqlite3.connect(db_path)

    cur = con.cursor()
    if (sys.argv[1] == "refresh_cloudflare"):
        if updateAllCloudflareIPs(cur):
            con.commit()
    elif (sys.argv[1] == "new_cloudflare" and len(sys.argv) == 3):
        list_name = sys.argv[2]
        new_list_id = None
        input(list_name)
        if not ( new_list_id := findListID(cur, list_name)):
            date_string = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            cur.execute(f"INSERT INTO access_list(created_on,modified_on,owner_user_id,name,meta) VALUES ('{date_string}','{date_string}',1,'{list_name}','{{}}')")
            new_list_id = cur.lastrowid
        insertIPs(cur, new_list_id, findOldCloudflareIps(cur))
        con.commit()
    elif (sys.argv[1] == "remove_cloudflare" and len(sys.argv) == 3):
        list_name = sys.argv[2]
        list_id = findListID(cur, list_name)
        if list_id:
            removeCloudflare(cur, list_id)
        con.commit()
    else:
        print("unrecognised command")
    con.close()

if __name__ == "__main__":
    main()