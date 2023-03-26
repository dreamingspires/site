---
title: "grant_remote_access: providing trusted remote assistance for Linux servers"
date: 2021-06-03
params:
  author: Edd Salkield
  img_caption: "/assets/portfolio/grant_remote_access/screenshot.png"
  description: "DreamingSpires team made it easy for clients to allow trusted access to their Linux servers so that the dev team can provide remote assistance while providing the client with complete control over the connection."
---

Research software projects are all about empowering research teams with the tools that they need; it’s one thing to have the code written, but it’s only useful once it’s understood by and integrated with the research group.
This presents a unique challenge for server-side applications, which often form a core piece of the research infrastructure but require specific technical skills to operate securely.

<script id="asciicast-2GwGhmjWMhLYCOJm4xXk3ifmn" src="https://asciinema.org/a/2GwGhmjWMhLYCOJm4xXk3ifmn.js" async></script>

To help address this problem, and to enable researchers to better take advantage of their organisation’s free or low-cost server computing facilities, we’ve created an open source tool, [_grant\_remote\_access_](https://gist.github.com/eddsalkield/fbbf892dff417cffb4aaac4b91062997), for temporary remote assistance of Linux servers.
If a host user runs the tool, it opens a tunnel through which authorised users at Dreaming Spires can temporarily log in to the system through a shared, monitored, and terminable session.
The host can monitor and view in real-time all the commands that are being run, and are fully empowered to close the session at any point.
The result is that we can provide secure remote access support on any Linux system, helping to train users as we go!

When invoked, _grant\_remote\_access_ sets up a temporary remote connection to our proxy server, and opens a secure remote access tunnel through it.
Access through the tunnel is restricted to our unique remote access key, to provide cryptographic guarantees about those who can log in.

Once a connection has been established, both parties end up in a shared [tmux](https://github.com/tmux/tmux) session, so that the commands that are executed are visible to both parties.
This is useful as a security measure, as well as aiding learning about the command-line nature of the system.

Finally, when the host closes the connection, or their terminal window, the remote tunnel is immediately closed.

Of course, _grant\_remote\_access_ is repurposable for any remote access use case by modifying the preloaded key and server details.
Feel free to play with it, and contribute back any changes you find useful!
