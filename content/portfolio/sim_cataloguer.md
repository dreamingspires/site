---
title: "Generating AI images inspired by authors' writing styles"
date: 2023-03-24
params:
    author: "Mark Todd, CEO and Software Developer"
    client: Digital Humanities, University of Southampton
    img_caption: "/assets/portfolio/sim_cataloguer/southampton_logo.png"
    description: "Packaging pixray and other gpt tools into a simple python interface"
---

For this project the overall aim was to produce a module that can generate images based on a the style of writing of a particular author. To do this it trained a model with GPT2 to mimic the author's writing style, then used the generated text as a prompt to generate an image.

The challenges of this project were unexpectedly entirely in the packaging process. The dependent packages were not setup to be simple to combine, but through several workarounds we succeeded in making a single package with all dependencies.

## Links

For the github repository, see here:

https://github.com/dreamingspires/simCataloguer
