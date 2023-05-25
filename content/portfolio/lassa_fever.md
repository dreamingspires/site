---
title: "Lassa Fever"
date: 2023-05-25
params:
    author: "Mark Todd, CEO and Software Developer"
    img_caption: "/assets/portfolio/default_portfolio.png"
    description: "The refactor of the lassa fever disease model"
---

As part of the Neglected Tropical Diseases projects, we refactored a model representing the lassa fever disease. This model was originally written in R, models the spread of the disease through a series of simulated "outbreaks". 

Originally these outbreaks were made such that time is iterated forward, and the outbreaks happen periodically. However, this was found to be very slow under certain model parameter values. For the refactor we instead simulated large portions of time at once, allowing for the use of large arrays. The vectorisation of this process increased the processing speed drastically. The model was originally refactored into python, and optimised, and later we translated this model back into R.

## Links

For the github repository, see here:

https://github.com/dreamingspires/lassa_fever

