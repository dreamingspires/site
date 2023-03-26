---
title: "Establishing Modular User Verification Systems with FastAPI-Users"
date: 2020-12-16
params:
  author: Mark Todd, Senior Engineer
  img_caption: "/assets/portfolio/fastapi_users/overall_architecture.png"
  description: "DreamingSpires team contributed to the user verification system in the  FastAPI-Users open-source project"
---

Dreaming Spires has begun work on an exciting new project - the Web Platform.
This will eventually allow the creation of a website with little initialisation.
But big things have small beginnings, and over the past couple of weeks we've started building the first component.

This component is called Users, and it is built upon the module FastAPI-Users to provide secure user login and authentication primitives.
However, in its current version, FastAPI-Users does not contain a method for user verification (required for users to be verified via email upon login), and required it to be built on top.

<img src="/assets/portfolio/fastapi_users/overall_architecture.png" alt="FastAPI Users Architecture">

_The overall architecture of the Web Platform, demonstrating the purpose of the Users component._

In line with our open source ethos, Dreaming Spires has submitted a pull request to this project, which will add a verification system for user login, based upon an idea laid out in [earlier community discussion](https://github.com/frankie567/fastapi-users/issues/106) within FastAPI-Users.
This will not only allow the Web Platform to benefit, but mean all future users will have the ability to implement their own custom verification systems.

Like the sound of the Web Platform? With our ever-advancing suite of web development components, we're in a good position to build your research-oriented site.
Register your interest with us to find out all we can do for you!

And for more info on FastAPI-Users, see its [official repository](https://github.com/frankie567/fastapi-users).
