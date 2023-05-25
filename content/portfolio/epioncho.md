---
title: "EPIONCHIO-Improvements"
date: 2022-12-15
params:
    author: "Mark Todd, CEO and Software Developer"
    img_caption: "/assets/portfolio/default_portfolio.png"
    description: "The optimisation of the EPIONCHO model"
---

Earlier this year we translated the EPIONCHO-IBM model from R to python, and restructured it's code to improve code clarity. In this project, we developed this further, to optimise the speed of the EPIONCHO model. This led us to vectorise many of the functions in the model.

The next bottleneck in the problem was the sampling of binomial distributions. We sped this up significantly, by pregenerating the samples using C++ bindings, and a new plugin called "Fast Binomial".

We also then abstracted the most generic parts of the disease model, into a separate library called "Endgame Simulations". The idea is that all of the code that can be applied to multiple diseases is kept in a separate repo, and becomes a module in itself.

Finally, we wished to make the structures of the model automatically serialisable in HDF5 format. These files are more compressed and transportable than the more typical pickle files, while also being inspectable. This led to the development of the "HDF5 Dataclass" module, that allows you to easily make dataclasses that support this form of file serialisation.

## Links

[Epioncho-IBM](https://github.com/dreamingspires/EPIONCHO-IBM)

[Fast Binomial](https://github.com/dreamingspires/fast-binomial)

[Endgame Simulations](https://github.com/dreamingspires/endgame-simulations)

[HDF5 Dataclass](https://github.com/dreamingspires/hdf5-dataclass)

[Pytest Trust Random](https://github.com/dreamingspires/pytest-trust-random)