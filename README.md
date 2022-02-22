# Dreaming Spires Site

Refactored [Dreaming Spires website](https://dreamingspires.dev), built as a
static site with [kiln](https://sr.ht/~adnano/kiln/), and styled with
[Bulma](https://bulma.io/).

Form submission handled via CORS request to [staticforms](https://github.com/dreamingspires/staticforms).

## Requirements

* [kiln](https://sr.ht/~adnano/kiln/)
* [npm](https://www.npmjs.com/)
* [sassc](https://github.com/sass/sassc)

## Building

```
npm install  # Install 
kiln build   #
```

To auto-rebuild on edit:

```
find . | entr -s 'kiln build && date && firefox $PWD/public/index.html'
```

TODO: determine how to refresh firefox without opening a new tab repeatedly

The built files will be in `./public`
