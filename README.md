# Dreaming Spires Site

Refactored [Dreaming Spires website](https://dreamingspires.dev), built as a static site with [kiln](https://sr.ht/~adnano/kiln/), and styled with [Bulma](https://bulma.io/).

Form submission handled via CORS request to [staticforms](https://github.com/dreamingspires/staticforms).

## Requirements

* [kiln](https://sr.ht/~adnano/kiln/)
* [npm](https://www.npmjs.com/)
* [sassc](https://github.com/sass/sassc)

## Building

`make all` will install and build everything, including the node packages.

`make site` will build just the site itself.

The built files will be in `./public`

To auto-rebuild on edit, run `./watch` in the root of the repository.

## Publishing

`make publish` will create a finished tarball of the site at `./site.tar.gz`.
This can be copied onto any web hosting server.
