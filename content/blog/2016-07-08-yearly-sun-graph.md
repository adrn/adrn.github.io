Title: Yearly sun graphs in Python
date: 2016-07-08 11:16
Category: tutorial
Tags: python, astropy
Slug: yearly-sun-graph
Authors: adrn

Molly Peeples ([@astronomolly](https://twitter.com/astronomolly)) recently tweeted [some really
cool plots](https://twitter.com/astronomolly/status/749675563539890176) from
[timeanddate.com](http://www.timeanddate.com/sun/uk/edinburgh) that visualize local solar
properties over a year from a location (e.g., twilights, solar noon, etc.), e.g.:

![alt text](/static/timeanddate.png "Edinburgh")


My first thought was: can we make those plots with Astropy? This post shows one way to make figures
like this in Python using [Astropy](http://www.astropy.org) and
[Matplotlib](http://www.matplotlib.org).

---

First, some imports:

{% notebook yearly-sun-graph.ipynb cells[0:] %}

---

Download the function to produce these plots [from this
Gist](https://gist.github.com/adrn/b1d7dcef1865777d40cbcd39ade9da65).

See the [full notebook
here](https://github.com/adrn/adrn.github.io-source/content/notebooks/yearly-sun-graph.ipynb).

