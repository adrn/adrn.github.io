Title: Making a Matplotlib animation with a transparent background
date: 2016-06-03 16:22
Category: tip
Tags: python, matplotlib
Slug: matplotlib-transparent-animation
Authors: adrn

I recently needed to overlay a Matplotlib animation on an image in a keynote
presentation. This requires creating an animation with a transparent background
so that only the plot elements are shown. It turns out that this is possible
using the Matplotlib animation objects (note: I've only tried this on Mac). The
key elements to doing this are to (1) make the Matplotlib figure background
invisible, (2) save the video using a png codec (yes, the image format), and (3)
to pass keyword arguments through the animation object to the individual
Matplotlib `savefig` calls. I'll show a simple example below of a circle
orbiting in a circle with a trail of points that fade out. *(Note: running this
code requires installing
[JSanimation](https://github.com/jakevdp/JSAnimation).)* First, imports:

{% notebook transparent-matplotlib-animation.ipynb cells[0:1] %}

We start by defining how many frames (timesteps) to use in the animation, and
how many circles to draw in the trail:

{% notebook transparent-matplotlib-animation.ipynb cells[1:2] %}

The circle will orbit in a circle:

{% notebook transparent-matplotlib-animation.ipynb cells[2:3] %}

Finally, the meat of the code containing the calls to Matplotlib:

{% notebook transparent-matplotlib-animation.ipynb cells[3:4] %}

Notice the lines that hide the plot elements and make the figure background
transparent:

```python
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_frame_on(False)
```

and

```python
fig.patch.set_alpha(0.)
```

To save the video out with a transparent background, the other critical
arguments are to the `save()` call, especially the keyword arguments passed
through via `savefig_kwargs`:

{% notebook transparent-matplotlib-animation.ipynb cells[4:5] %}
