---
title: "Erotetic theory and human reasoning in python"
date: 2023-12-02
params:
    author: "Mark Todd, CEO and Software Developer"
    client: Faculty of Philosophy, University of Oxford
    client_url: https://www.philosophy.ox.ac.uk/
    img_caption: "/assets/portfolio/default_portfolio.png"
---

The book "Reason and Inquiry: The Erotetic Theory" by Philipp Koralus presents a mathematical representation of human reasoning and decision making. In this project we converted the mathematical representation from the book into python functions.

This included developing a string parser to go to and from various compact forms in first order logic, into an internal object representation. Once in this object form, set operations and various mathematical operations can then be done. We described the objects expressed in first order logic as classes, and the custom operations between objects as methods. Finally the object representation is then translated back to string form for inspection.

Each example from the book was also translated into a unit test to allow users to easily compare the two, and also as a method of asserting correctness between the book and the model.

We look forward to further developments on this project, and its upcoming release.

Codebase: Pending Release
