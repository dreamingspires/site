---
title: "Project Spotlight: auction-scraper"
date: 2020-09-07
params:
  author: "Edd Salkield"
  img_caption: "/assets/portfolio/project_spotlight_auction_scraper/blog_banner.jpg"

---

<img src="/assets/portfolio/project_spotlight_auction_scraper/blog_banner.jpg">

This project spotlight is dedicated to _[auction-scraper](https://dreamingspires.dev/github.com/dreamingspires/auction-scraper)_, an open source, extensible auction house scraper for ebay, liveauctioneers, and other platforms.
Built for the [School of Anthropology at the University of Oxford](https://www.anthro.ox.ac.uk/), it serves as a fantastic example of how computational talent can bring tremendous value in unlikely places!

<div class="card mr-3 has-background-primary-dark" style="float: left; width:60%">
  <div class="card-content">
    <script id="asciicast-kzp1Opc78N2uyYBlQiApiJllw" src="https://asciinema.org/a/kzp1Opc78N2uyYBlQiApiJllw.js" async></script>
  </div>
  <footer class="card-footer">
    <p class="card-footer-item has-text-light">
      Screencast of a terminal session with auction-scraper.
    </p>
  </footer>
</div>

The project aim was to build a complete picture of the sale of African tribal art by online vendors, allowing further data-driven research into the communities and the markets surrounding them.
These online vendors often make use of auction houses to sell the artwork; however, it quickly became apparent that nobody had yet built a general-purpose auction scraping tool with the capabilities we required.
It subsequently became our mission to build the best auction house scraping system on the internet.

We started by cleaning the many disparate, manually gathered data sets that had already been gathered by the client.
We settled on a relational database schema that captured the relationship between auctions and their sellers, as to also allow us to fill out the database automatically from our scraper.

Utilising Python as the development language for the project, we set to work designing an abstract scraper class which would provide a uniform interface for each auction house back-end.
This also allowed us to elegantly reuse code that's relevant to all auction sites.
We implemented this class for the ebay, liveauctioneers, and catawiki sites, which are at the time of writing have the most prevalent selection of tribal art available.

The implemented auction scraper classes were then tied together with a consistent, easy-to-use command-line interface.
Individual pages can be scraped given their auction ID, URL, or even a saved file on disk.
Alternatively, searches can be conducted given a query, with all resulting auction and profile pages being scraped.

The scraped data is placed into a sqlite database, making use of [SQLAlchemy](https://www.sqlalchemy.org/) to merge older scraped data with the most up-to-date results.
Additional data, such as images and the downloaded pages themselves, can be placed within a data directory and are referenced from the database itself.

### Packaging and distribution

To make installation easy, we have packaged the project for distribution via [PyPI](https://pypi.org/), the Python Package Index, making installation as simple as:

```
pip install --user auction-scraper
```

We made use of the cutting-edge [poetry](https://python-poetry.org/) build system to automate the process of building the packages, making deployment and distribution of updates easy.
The project is open source, so if you'd like to build the project yourself you can simply follow the build instructions in the [README](https://github.com/dreamingspires/auction-scraper/blob/master/README.md).

In all, this has been a really fascinating project to get involved with, and we can't wait to see the results of the research as the data set grows and the scraper sees wider adoption.
Indeed, feel free to download auction-scraper yourself and give it a try.

### Need to develop CLI tools?

Whether you require a quick script to clean your data set, or want to see your research tooling be as scriptable and useful as possible, we have you covered.
Our developers have experience in packaging software for the command line, and building flexible interfaces for future reuse in new situations.
If this interests you, simply [register your project](https://dreamingspires.dev/auth/register_client/#signup) with us to get started!
