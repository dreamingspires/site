# Dreaming Spires Site

This is the source code to the Dreaming Spires website, hosted at https://dreamingspires.dev.  It is licensed under Creative Commons BY 4.0, giving you the freedom to share and adapt this work provided that appropriate credit is given.
More details can be found at https://creativecommons.org/licenses/by/4.0/.

This website is entirely static, meaning that it exists in compiled form as a set of unchanging HTML, CSS, and Javascript files.
This makes it easy to maintain, boasting speedy loading times, low resource requirements, compatibility with every browser, and good accessibility.
As a result, this website can run basically anywhere, even on the cheapest VPS instances available.

Dynamic content, such as form uploads and interfacing with git providers for the admin interface, are provided by minimal server processes which each handle that one job.

## Technical details

Built as a static site with [kiln](https://sr.ht/~adnano/kiln/), and styled with [Bulma](https://bulma.io/), with sass packages pulled in through [npm](https://www.npmjs.com/).
Form submission handled via CORS request to [staticforms](https://github.com/dreamingspires/staticforms).

## Requirements

* [kiln](https://sr.ht/~adnano/kiln/) - the static site generator
* [npm](https://www.npmjs.com/) - used to pull in stylesheet dependencies
* [sassc](https://github.com/sass/sassc) - used to compile the stylesheets
* [entr](https://eradman.com/entrproject/) - used for watch.sh to rebuild files as they change
* [imagemagick](https://imagemagick.org/) - used to compress images

Install these preferably with your system package manager.

## Building

`make all` will install and build everything, including the node packages.

`make site` will build just the site itself.

The built files will be in `./public`

To auto-rebuild on edit, run `./watch` in the root of the repository.

## Running a local instance of the site

```sh
./serve
```

Then navigate to http://localhost:9000

## Publishing

`make publish` will create a finished tarball of the site at `./site.tar.gz`.
This can be copied onto any web hosting server.
