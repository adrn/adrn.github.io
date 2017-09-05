Title: AAS227 Hack Day: Towards optimal AAS session scheduling
date: 2016-01-13 10:00
Category: hack
Tags: hackday, aas, aas227, machinelearning
Slug: aas-session-scheduling1
Authors: adrn

Last week was another winter meeting of the American Astronomical Society
(AAS227) and another installment of the [AAS Hack
Day](http://www.astrobetter.com/wiki/AASHackDay). Earlier in the week, I gave a
short 5 minute talk on [Software
Testing](https://speakerdeck.com/adrn/software-testing) and participated in a
panel on better practices for scientific programming, then gave my [Dissertation
talk](https://speakerdeck.com/adrn/chaos-and-stellar-streams) on the density
evolution of stellar streams formed around chaotic orbits. At the hack day, I
worked with Scott Idem (AAS) and David W. Hogg (NYU) to continue the theme of
hacks [started 2 years
ago](http://www.astrobetter.com/blog/2014/01/22/aas-hack-day-2014/) by Dan
Foreman-Mackey (UW), Dylan Gregersen (UU), and I working with all titles and
abstracts presented at the AAS meeting.

The idea for this year was to work towards automating the scheduling process for
the AAS meetings. Right now (as far as I know) submitted abstracts are sorted
manually by volunteers and then organized into sessions. I'm not sure how much
thought goes in to scheduling simultaneous sessions, but I know that for my own
interests there are often multiple sessions happening at the same time (leading
to "session jumping"). Maybe computers can do better?

The AAS (really: Scott Idem, facilitated by Kelle Cruz - thanks!) gave us access
to a database containing session and presentation info for AAS227 and past
meetings. This was a huge improvement from previous hack days where
Foreman-Mackey spent most of his time parsing the abstract info from a PDF (if I
remember correctly). With access to the database, we set off to do some proof of
concept hacks with the text data. Below I've included cells from the Jupyter
notebook I worked in during the hack day:

{% notebook aas-abstract-similarity.ipynb cells[5:] %}
