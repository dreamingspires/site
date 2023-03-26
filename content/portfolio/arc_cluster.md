---
title: "Running code at Supercompute Scale on the ARC Cluster"
date: 2020-11-03
params:
  author: "Edd Salkield"
  img_caption: "/assets/portfolio/arc_cluster/over-arctic_0.jpg"
  description: "Successfully and reliably deploying the Auction Scraper application on the ARC Supercomputing cluster for the Department of Anthropology at University of Oxford"
---

<img src="/assets/portfolio/arc_cluster/over-arctic_0.jpg" alt="ARC cluster">

_Banner photo courtesy of Oxford's [Advanced Research Computing division](https://www.arc.ox.ac.uk/overview)._

Success for any software project begins with a well-planned launch.
It's one thing to have the code written, but it’s only useful once you can use it.
That's why we've been working with the Department of Anthropology at the University of Oxford to deploy our auction scraper platform, for reliably tracking and processing the sale of African tribal art online, on the university's research computing infrastructure.

Keeping data sets up to date with regularly scheduled and parallelisable data processing tasks was a requirement for this project.
We sought to achieve these aims using the resources available at the university; ARC, the [Advanced Research Computing cluster](https://www.arc.ox.ac.uk/).

ARC is a High Performance Computing (HPC) system, in which individual jobs can be scheduled to be run across multiple nodes, kept in sync with a consistent back-end database.
To run our job across the cluster, a script for the SLURM task scheduler was written, which invokes the program with the correct arguments to scrape and process the relevant data.
An auto-mailer was set up to notify the researchers of failing tasks, which proved useful in our beta testing phase to ensure stability, even as the underlying auction sites adjusted their layout.

A sqlite database was set up in a shared data area, which exposes a common interface among the nodes in the cluster, alongside directories for scraped site metadata, such as images and page backups.

Our code has been running successfully on ARC for several months, with a very high stability rate.
Where changes in the underlying auction site caused exceptions, our code failed gracefully, giving our engineers time to resolve the issue through a patch the following day.

At Dreaming Spires, we're dedicated to helping your project succeed.
That's why we offer a free three-month bug testing period with all of our projects be default, and will help you set up hosting long term - whether that's with us, or your institituion.
Our experienced engineers will be able to advise you as to what hosting methods best suit your needs.
