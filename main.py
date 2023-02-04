import math
import random

import pgzrun

"""CONFIGURATION"""

WIDTH = 800
HEIGHT = 800
COUNT = 80
MINRADIUS = 10
MAXRADIUS = 25
MAXFORCE = 200
BG = "#F0F8FB"

"""VARIABLES"""

particlesList = []  # List of particles


"""DRAW"""


def draw():
    screen.fill(BG)
    drawParticles()


def drawParticles():
    for particle in particlesList:
        screen.draw.filled_circle(
            (particle["x"], particle["y"]), particle["radius"], particle["color"])


"""UPDATE"""


def update():
    updateParticles()


def updateParticles():
    computeForces()
    applyForces()


"""HELPERS"""


def computeForces():
    for i in range(len(particlesList)):
        for j in range(i + 1, len(particlesList)):
            particle1 = particlesList[i]
            particle2 = particlesList[j]
            diffX = particle2['x'] - particle1['x']
            diffY = particle2['y'] - particle1['y']
            distance = math.sqrt(diffX ** 2 + diffY ** 2)
            if distance == 0:
                continue

            force = -1 * particle1['charge'] * \
                particle2['charge'] / (distance * distance)
            force = min(force, MAXFORCE)

            forceX = force * diffX / distance
            forceY = force * diffY / distance

            particle1['forceX'] += forceX
            particle1['forceY'] += forceY
            particle2['forceX'] -= forceX
            particle2['forceY'] -= forceY


def applyForces():
    for particle in particlesList:
        particle['vx'] += particle['forceX'] / particle['mass']
        particle['vy'] += particle['forceY'] / particle['mass']
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        particle["forceX"] = 0
        particle["forceY"] = 0
        containParticle(particle)


def containParticle(particle):
    if particle['x'] < particle["radius"]:
        particle['x'] = particle["radius"]
        particle['vx'] = math.fabs(particle['vx'])
    if particle['y'] < particle["radius"]:
        particle['y'] = particle["radius"]
        particle['vy'] = math.fabs(particle['vy'])
    if particle['x'] > WIDTH - particle["radius"]:
        particle['x'] = WIDTH - particle["radius"]
        particle['vx'] = math.fabs(particle['vx']) * -1
    if particle['y'] > HEIGHT - particle["radius"]:
        particle['y'] = HEIGHT - particle["radius"]
        particle['vy'] = math.fabs(particle['vy']) * -1


def randomPastelColor():
    """Returns a random pastel color in the form of a RGB tuple."""

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    while abs(R + G + B - 255) < 10:
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

    return (R, G, B)


"""INITIALIZATION"""


def init():
    global particlesList

    particlesList = [{
        "radius": random.randint(MINRADIUS, MAXRADIUS),
        "x": random.randint(0, WIDTH),
        "y": random.randint(0, HEIGHT),
        "color": randomPastelColor(),
        "vx": 0,
        "vy": 0,
        "forceX": 0,
        "forceY": 0,
    } for _ in range(COUNT)]

    for particle in particlesList:
        particle["mass"] = particle["radius"]
        particle["charge"] = particle["mass"] * 2


init()
pgzrun.go()
