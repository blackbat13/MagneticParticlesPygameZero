import math
import random

import pgzrun

"""CONFIGURATION"""

WIDTH = 800
HEIGHT = 800
COUNT = 20
MAXRADIUS = 20
MINRADIUS = 5
MINMASS = 5
MAXMASS = 20

"""VARIABLES"""

particlesList = []  # List of particles


"""DRAW"""


def draw():
    screen.fill("white")
    drawParticles()


def drawParticles():
    for particle in particlesList:
        screen.draw.filled_circle(
            (particle["x"], particle["y"]), particle["radius"], particle["color"])


"""UPDATE"""


def update():
    pass

def updateParticles():
    pass

"""HELPERS"""


def randomColor():
    """Returns a random color in the form of a RGB tuple."""

    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


"""INITIALIZATION"""


def init():
    global particlesList

    particlesList = [{
        "radius": random.randint(MINRADIUS, MAXRADIUS),
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "color": randomColor(),
        "mass": random.randint(MINMASS, MAXMASS),
        "vx": 0,
        "vy": 0,
    } for _ in range(COUNT)]


init()
pgzrun.go()
