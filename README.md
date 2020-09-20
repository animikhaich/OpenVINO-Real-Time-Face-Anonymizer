[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="assets/face_ai.png" alt="Logo" width="150" height="150">

  <h2 align="center">Real Time Face Blur Algorithm</h2>

  <p align="center">
    Blur Faces in Real-Time while processing on a single CPU. Make your videos GDPR compliant in minutes.
    <br />
    <a href="https://youtu.be/sTswDfqWowg">View Demo</a>
    ·
    <a href="https://github.com/animikhaich/VTU-Result-Downloader/issues/new">Report Bug</a>
    ·
    <a href="https://github.com/animikhaich/VTU-Result-Downloader/issues/new">Request Feature</a>
  </p>
</p>
<p align="center">
  <img src="assets/face-blur-demo.gif" alt="Demo GIF">
</p>
<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Demo](#demo)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Built With](#built-with)
  - [Minimum Hardware Requirements](#minimum-hardware-requirements)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
    - [Animikh Aich](#animikh-aich)

<!-- ABOUT THE PROJECT -->

## About The Project

A web-scraping program to automatically download VTU University Results for specified USN numbers. This was originally created for the use in Dept. of ECE, RNS Institute of Technology.

Unfortunately, the VTU results website has been drastically modified, and I do not have time to maintain this project any further. Hence, this project is deprecated and it no longer works. However, for reference in terms of code, it is published and the code is publicly available. Any contributions are welcome.

## Demo

-   [YouTube Video](https://youtu.be/sTswDfqWowg)

<!-- GETTING STARTED -->

## Getting Started

At the moment, the GUI Runs but the functional part is broken (since the website has been modified). You can still try out the code, or contribute. Just clone the repository, install the dependencies and start using it.

### Prerequisites

-   [Python 3](https://www.python.org/)
-   [Git](https://git-scm.com/)

### Built With

I wanted to reduce the file-size for this simple project. Hence, I used Tkinter instead of PyQT5.

-   [PyQt5](https://pypi.org/project/PyQt5/)
-   [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
-   [Requests](https://requests.readthedocs.io/en/master/)
-   [Pandas](https://pandas.pydata.org/)

### Minimum Hardware Requirements

-   CPU: 1 Logical Cores (Threads)
-   RAM: 500 MB
-   Storage: 500 MB (Including Dependencies)
-   OS: Linux, Windows, MacOS

### Installation

1. Clone the repo

```sh
git clone https://github.com/animikhaich/VTU-Result-Downloader.git
```

2. Install Python packages

```sh
pip install -r requirements.txt
```

1. Run the main file

```sh
python GUI.py
```

<!-- USAGE EXAMPLES -->

## Usage

There are two buttons and a dropdown selector (Deprecated).

-   Select whether you want to fetch results for CBCS or Non-CBCS scheme.
-   Enter the USN Range (Start and end), and select the filename and/or file location.
-   Click on Download.

<!-- CHANGELOG -->

<!-- ROADMAP -->

## Roadmap

This project is **No Longer Maintained by me**. Contributions are welcome.

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

<!-- CONTACT -->

## Contact

#### Animikh Aich

-   Website: [Animikh Aich - Website](http://www.animikh.me/)
-   LinkedIn: [animikh-aich](https://www.linkedin.com/in/animikh-aich/)
-   Email: [animikhaich@gmail.com](mailto:animikhaich@gmail.com)
-   Twitter: [@AichAnimikh](https://twitter.com/AichAnimikh)

<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/animikhaich/VTU-Result-Downloader.svg?style=flat-square
[contributors-url]: https://github.com/animikhaich/VTU-Result-Downloader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/animikhaich/VTU-Result-Downloader.svg?style=flat-square
[forks-url]: https://github.com/animikhaich/VTU-Result-Downloader/network/members
[stars-shield]: https://img.shields.io/github/stars/animikhaich/VTU-Result-Downloader.svg?style=flat-square
[stars-url]: https://github.com/animikhaich/VTU-Result-Downloader/stargazers
[issues-shield]: https://img.shields.io/github/issues/animikhaich/VTU-Result-Downloader.svg?style=flat-square
[issues-url]: https://github.com/animikhaich/VTU-Result-Downloader/issues
[license-shield]: https://img.shields.io/github/license/animikhaich/VTU-Result-Downloader.svg?style=flat-square
[license-url]: https://github.com/animikhaich/VTU-Result-Downloader/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/animikh-aich/
[product-screenshot]: assets/face-blur-demo.gif
