---
title: "Oxford Mindmap: mobile app for sharing mental health experiences"
date: 2020-10-01
params:
  author: "Edd Salkield"
  client: Oxford Ideas Festival
  client_url: https://if-oxford.com/welcome-page/
  img_caption: "/assets/portfolio/project_spotlight_oxford_mindmap/in_range.png"
  description: "Oxford Mindmap is a mobile app designed and built by Dreaming Spires in partnership with Oxford Ideas Festival to provide a new perspective on the city of Oxford. As users explore its locations and its buildings, they can also relate to personal stories of mental health submitted anonymously by its users."
---

We are excited to announce the release of the latest mobile app developed by Dreaming Spires:

### _Oxford Mindmap - Tell us your story!_

From today, it's available on all major mobile app stores.

<div class="columns is-centered">
  <div class="column is-flex" style="justify-content: center">
    <a href="https://apps.apple.com/gb/app/oxford-mindmap/id1532875106">
      <img src="/assets/portfolio/project_spotlight_oxford_mindmap/app-store-badge.png" alt="Apple AppStore badge" width="152" height="45">
    </a>
  </div>
  <div class="column is-flex" style="justify-content: center">
    <a href="https://play.google.com/store/apps/details?id=dev.dreamingspires.oxford_mindmap">
      <img src="/assets/portfolio/project_spotlight_oxford_mindmap/play-store-badge.png" alt="Google Playstore badge" width="152" height="45">
    </a>
  </div>
</div>

Created in partnership with the [Oxford Ideas Festival](https://if-oxford.com/events/), _Oxford Mindmap_ is designed to give a new perspective on the city of Oxford.
Through the app, users can explore Oxford, its locations and its buildings, as they relate to personal stories of mental health submitted anonymously by its users.

<div class="card mr-3 has-background-primary-dark" style="float: left; width:60%">
  <div class="card-content">
    <figure class="image">
    <img style="width: 60%" src="/assets/portfolio/project_spotlight_oxford_mindmap/in_range.png" alt="Screenshot of the app showing a story being unlocked as a user crosses Magdalen bridge">
</figure>
  </div>
  <footer class="card-footer">
    <p class="card-footer-item has-text-light">
      A story is unlocked as a user crosses Magdalen bridge
    </p>
  </footer>
</div>

Users can explore an interactive map of the city scattered with map markers, one for each story.
The stories are unlockable only when the user is physically within range, encouraging exploration of the city in a new way.
Since each story has a unique connection with its location, users can experience first-hand the sights and atmosphere in the mind of each author.

Once unlocked, stories are viewable at any time from the _Unlocked Stories_ tab.
To recapture the feeling of the location, an appropriate banner image is displayed alongside it.

Since the stories pertain in particular to mental health, it's appropriate that users should be aware up-front of stories that broach difficult topics.
Therefore, each story can be tagged with trigger warnings.
Through the settings menu, users can specify whether there are particular tags which they'd rather not be exposed to.
Such stories are subsequently hidden from view.

<div class="card mr-3 has-background-primary-dark" style="float: right; width:70%">
  <div class="card-content">
    <figure class="image mx-0">
    <img src="/assets/portfolio/project_spotlight_oxford_mindmap/admin_console.png" alt="Screenshot of the admin console used to modify story information on-the-fly">

</figure>
  </div>
  <footer class="card-footer">
    <p class="card-footer-item has-text-light">
      The admin console is used to modify story information on-the-fly
    </p>
  </footer>
</div>

Users can also submit their own anonymous stories through an embedded form.
The stories are staged for review, and can then be uploaded for viewing in the app in real time through an admin console on the server.

We encourage you to check out _Oxford Mindmap_ if you're ever in Oxford, and want to explore the city in the footsteps of other people who came before.
In particular, if you're interested in submitting a story of your own, we encourage you to [fill in the form](https://client.dreamingspires.dev/oxford-mindmap/submit-story).
Your story will be reviewed, and might even be chosen for inclusion!

### The tech specs

We love open source software, so you can find the source code for the project [here](https://dreamingspires.dev/github.com/dreamingspires/Oxford-Mindmap)!

In the back end, a cloud server has been deployed using Dreaming Spires hosting which exposes an API to get the story data.
The story data itself is backed up regularly to insure against data loss.
Stories can be added to and removed from the database, and edited with a finer granularity, using the easy-to-use admin panel.

The app itself is built with [Expo](https://expo.io/), and regularly polls the server to check for story updates, completing the over-the-air update system.
To preserve user privacy, all processing related to the user location, such as the locking and unlocking of stories, is done client-side.

### Interested in mobile development?

Whatever your project requirements, front or back end, we're sure to be able to find the right software solution to suit your needs.
So go on, simply [register your project with us](https://dreamingspires.dev/auth/register_client/#signup) to get started!
