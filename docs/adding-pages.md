# Adding Pages to Portfolio

One can add a blog post to the portfolio page by adding a Markdown file to the [`content/portfolio`](../content/portfolio/) directory. `kiln` and `mdtohtml` takes care of converting it into a HTML page and adding it to the main Portfolio page.

The author must provide additional metadata as YAML at the top of the markdown file to provide the necessary information for generating the final HTML page. This is referred to as `frontmatter` in kiln.

```yaml
---
title: required # Used in the page as well as in the meta tags
date: required # YYYY-MM-DD Used to order the pages in reverse chronological order and in permalinks
template: optional # Selects the template to render the page with. Uses _page.html under templates/portfolio/ by default for blog posts
weight: optional # Useful in sorting pages (lowest first) in addition to the date
params:
    author: required
    img_caption: required # Used as cover image in the card on portfolio page
    description: optional # Used in the page meta tags if provided. Useful in SEO

    # Other fields can be added here and can be used inside the template
---
```

You can directly add images, video and other elements to the markdown post using the respective HTML tag. If a local file needs to be included in the blog post, create a directory under [static/assets/portfolio/](../static/assets/portfolio/) and add your images to this directory. `kiln` will move it to the final assets directory and make it available at under the absolute url `/assets/portfolio/{{ DIR }}/{{ IMAGE }}`. Make sure to add alt tag to the media elements in the HTML as best practice.

## Example
1. Add the following markdown `example.md` to [`content/portfolio/`](../content/portfolio/)
```md
---
title: "Example blog post"
date: "2023-03-26"
params:
    author: "IMG-PRCSNG"
    img_caption: "/assets/portfolio/example/caption.jpg"
    description: "This is an example blog post"
---
<img src="/assets/portfolio/example/banner.jpg" alt="Banner image"/>

This is an example blog post with a banner image
```

2. Add the images (banner.jpg, caption.jpg) associated with the blog post to a directory, say `example`, under [static/assets/portfolio/](../static/assets/portfolio/). Images will be available under `/assets/portfolio/example/` url.

3. Run `make site`

The page will be generated in the directory [`public/portfolio/example`](../public/portfolio/example). A card will be added to the `/portfolio` page and the blog can be accessed with the url `/portfolio/example/`