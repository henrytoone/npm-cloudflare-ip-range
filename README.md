<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Nginx Proxy Manager Access List Cloudflare Updater</h3>

  <p align="center">
    A script to create and update Nginx Proxy Manager access lists with Cloudflare's current IP ranges.
    <br />
    <a href="https://github.com/henrytoone/npm-cloudflare-ip-range/wiki"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/henrytoone/npm-cloudflare-ip-range/issues">Report Bug</a>
    ·
    <a href="https://github.com/henrytoone/npm-cloudflare-ip-range/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://github.com/henrytoone/npm-cloudflare-ip-range) -->

Nginx Proxy Manager currently does not have a way of automating the process of creating an access list with the current cloud flare orange cloud ips. I couldn't find a way of doing this that tied together the UI with the actual config files so I created a script to do it for you.

This script was created in an afternoon and is most likely is missing something so feel free to open an issue or create a PR for any bugs or feature requests.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://python.org/)
* [SQLite](https://sqlite.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
Assuming that python is already installed >= 3.8 and a working setup of Nginx Proxy Manager is already running

* requests and toml module
  ```sh
  $ pip install -r requirements.txt
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   $ git clone https://github.com/henrytoone/npm-cloudflare-ip-range.git
   ```
2. Enter your database path into  `config.toml`
   ```toml
   db_path = './database.sqlite'
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### _After running the script you must go into the web interface to each affected list and click save_

### Add Cloudflare IPs to list
```
$ sudo python access_util.py new_cloudflare mylist
```

### Update with latest cloudflare IPs

```bash
$ sudo python access_util.py refresh_cloudflare
```

### Remove Cloudflare IPs from a list
```bash
$ sudo python access_util.py remove_cloudflare mylist
```

_For more examples, please refer to the [Wiki](https://github.com/henrytoone/npm-cloudflare-ip-range/wiki/Examples)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add more validation
- [ ] Remove need to `Save` on web interface
- [ ] More helpful debug information
- [ ] Better handling of arguments
- [ ] Support for older versions of python

See the [open issues](https://github.com/henrytoone/npm-cloudflare-ip-range/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Henry Toone - [GitLab](https://gitlab.com/henrytoone) - [GitHub](https://github.com/henrytoone) - hello@henrytoone.com

Project Link: [https://github.com/henrytoone/npm-cloudflare-ip-range](https://github.com/henrytoone/npm-cloudflare-ip-range)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/henrytoone/npm-cloudflare-ip-range.svg?style=for-the-badge
[contributors-url]: https://github.com/henrytoone/npm-cloudflare-ip-range/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/henrytoone/npm-cloudflare-ip-range.svg?style=for-the-badge
[forks-url]: https://github.com/henrytoone/npm-cloudflare-ip-range/network/members
[stars-shield]: https://img.shields.io/github/stars/henrytoone/npm-cloudflare-ip-range.svg?style=for-the-badge
[stars-url]: https://github.com/henrytoone/npm-cloudflare-ip-range/stargazers
[issues-shield]: https://img.shields.io/github/issues/henrytoone/npm-cloudflare-ip-range.svg?style=for-the-badge
[issues-url]: https://github.com/henrytoone/npm-cloudflare-ip-range/issues
[license-shield]: https://img.shields.io/github/license/henrytoone/npm-cloudflare-ip-range.svg?style=for-the-badge
[license-url]: https://github.com/henrytoone/npm-cloudflare-ip-range/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=2867B2
[linkedin-url]: https://www.linkedin.com/in/henrytoone/
[product-screenshot]: images/screenshot.png
