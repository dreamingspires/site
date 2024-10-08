---
title: "Redeveloping mass spectrometry tools for paleoproteomic applications"
date: 2020-09-21
params:
  author: "Edd Salkield"
  client: Max Planck Institute
  img_caption: "/assets/portfolio/project_spotlight_mmass/blog_banner.jpg"
  description: "Dreaming Spires updated mMass, a mass spectrometry toolkit, and made it easy to run it on modern operating systems and architectures."
---

<img src="/assets/portfolio/project_spotlight_mmass/blog_banner.jpg" alt="">

Today we dive straight into scientific research as we look at [mMass](https://github.com/dreamingspires/mMass), a mass spectrometry toolkit for chemical analysis, and how Dreaming Spires has been working to overhaul the program to run on modern operating systems.
mMass has been discontinued now for seven years and so fails to execute on most computers due to the age of its libraries.
Despite this, it still finds daily use both in the [Max Planck Institute](https://www.shh.mpg.de/en), Berlin (our wonderful client!), and more broadly in the Chemistry community.

We've taken it upon ourselves to revive mMass to its former glory.

### The Python2 problem

Since 2014, Python 2.7 has been in the process of being deprecated in favour of Python 3, with the final sunset date having been [earlier this year](https://www.python.org/dev/peps/pep-0373/#update).
In the transition from Python 2 to Python 3, [many breaking changes](https://www.wxpython.org/Phoenix/docs/html/MigrationGuide.html) were made to the language specification to keep Python more consistent and useful into the future.

However, where there are breaking changes, there are also projects that lack maintainers that start breaking.
With operating system vendors requiring that software does not depend upon Python 2 where possible, and many people no longer running Python 2 interpreters on their machines, projects like mMass became harder to run.

Breaking changes also affected the Python extension modules interface, where code written in other languages to interface with the interpreter became unusable throughout the update.
Additionally, many libraries took the opportunity of this transition period to overhaul themselves and push through fundamental changes.
Both of these further issues affected mMass.

Due to the intensive nature of the computation being performed, mMass has an extension module written in C to improve the speed of bottle-necking calculations.
Also, mMass has traditionally relied on wxPython which finds its new incarnation as wxPython Project Phoenix, in itself making many breaking changes (many of which not listed in the migration guide).
All of this made mMass a particularly difficult piece of software to port.

### The overhaul plan

Working with the Max Planck Institute to identify particular areas of the software that required attention, we planned out the requirements of the new version of mMass.
In addition to resolving the issues following on from Python2, we were to redesign the Python extension modules interface and port wxPython-specific code across to its latest version.

We planned to take the opportunity to overhaul the build system, making use of [poetry](https://python-poetry.org/) to manage build dependencies and the external compilation and linking of the C library.
Also critical to the success of the project was time spent packaging the software to make it portable across many operating systems, with good documentation to make it easy to maintain in the future.
The results

Today, mMass can run once again on any system that can use the [pip](https://pip.pypa.io/) package manager, with a Windows installer also provided while [winget](https://github.com/microsoft/winget-cli) still finds its feet.
But despite our success so far, we're not done yet!

We're still working on a native MacOS build, and we might well be working on a documentation overhaul and implementing additional features in time to come.
Need to have old software ported?

Are mission-critical tools within your organisation starting to creak at the seams? Whether due to changing libraries, a lack of a maintainer, or simply needing to be ported to run on different hardware, Dreaming Spires can help.

We'll link you with developers experienced in software porting, who can update the libraries and refresh the code to get it running and future-proofed.
Whatever your programming needs, you can simply [register your project with us](https://dreamingspires.dev/auth/register_client/#signup) to get started!
