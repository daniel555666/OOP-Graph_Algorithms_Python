import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab

matplotlib.use("Agg")

plt.rcParams.update({
    "lines.marker": "o",         # available ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
    "lines.linewidth": "1.8",
    "axes.prop_cycle": plt.cycler('color', ['white']),  # line color
    "text.color": "white",       # no text in this example
    "axes.facecolor": "black",   # background of the figure
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",  # no labels in this example
    "axes.grid": "True",
    "grid.linestyle": "--",      # {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "figure.facecolor": "black", # color surrounding the plot
    "figure.edgecolor": "black",
})

fig = pylab.figure(figsize=[4, 2], # Inches
                   dpi=100)        # 100 dots per inch, so the resulting buffer is 400x200 pixels
fig.patch.set_alpha(0.1)           # make the surrounding of the plot 90% transparent to show what it does

ax = fig.gca()
ax.plot([1, 2, 4,9,500,1000,100])


canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.buffer_rgba()

pygame.init()
window = pygame.display.set_mode((600, 210), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()
surf = pygame.image.frombuffer (raw_data, size, "RGBA")

bg_color = (204, 255, 204)   # fill red as background color
screen.fill(bg_color)
screen.blit(surf, (100, 5)) # x, y position on screen
pygame.display.flip()

stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    pygame.time.Clock().tick(30)  # Avoid 100% CPU usage