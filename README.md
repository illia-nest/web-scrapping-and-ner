<a id="readme-top"></a>




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="120" height="120">
  </a>

  <h3 align="center">AI Project #1: </h3>
  <h2 align="center">Web Scraping and Named Entity Recognition using Python</h2>

  <p align="center">
    by Illia Nesterenko
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

This project grew from an academic assignment I had to do as a grad student. In short, I have extracted the named entities (e.g. "United Nations", "Macron" etc) from 13 Wikipedia articles 
on the topic of the Russo-Ukrainian war (<i>phase 1-2</i>). Then, I constructed a graph to visualize which entities were the most connected across the corpus (<i>phase 3</i>). Finally, I ran several clusterization algorithms to
group the words that are locally closer to each other (<i>phase 4</i>). In the end, I compiled the whole code into a single file (<i>phase 5</i>).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
* [![numpy]][numpy-url]
* [![pandas]][pandas-url]
* [![sklearn]][sklearn-url]
* [![matplotlib]][matplotlib-url]
* [![networkX]][networkX-url]
* [![nltk]][nltk-url]
* [![spacy]][spacy-url]
* [![requests]][requests-url]
* [![wikipediaapi]][wikipediaapi-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->

[requests]: https://img.shields.io/badge/requests-gray?style=for-the-badge
[requests-url]: https://requests.readthedocs.io
[wikipediaapi]: https://img.shields.io/badge/wikipedia--api-brown?style=for-the-badge
[wikipediaapi-url]: https://pypi.org/project/Wikipedia-API/
[nltk]: https://img.shields.io/badge/nltk-darkgreen?style=for-the-badge
[nltk-url]: https://nltk.org/
[spacy]: https://img.shields.io/badge/spacy-blue?style=for-the-badge
[spacy-url]: https://spacy.io/
[NetworkX]: https://img.shields.io/badge/networkx-purple?style=for-the-badge
[NetworkX-url]: https://networkx.org/
[numpy]: https://img.shields.io/badge/numpy-%23013343?style=for-the-badge&logo=numpy
[numpy-url]: https://numpy.org/
[pandas]: https://img.shields.io/badge/pandas-%23130654?style=for-the-badge&logo=pandas
[pandas-url]: https://pandas.pydata.org/
[matplotlib]: https://img.shields.io/badge/matplotlib-%230060df?style=for-the-badge&logo=matplotlib
[matplotlib-url]: https://matplotlib.org/
[sklearn]: https://img.shields.io/badge/scikit--learn-%23223228?style=for-the-badge&logo=scikitlearn
[sklearn-url]: https://scikit-learn..org/
