#!/usr/bin/env python
import svgwrite
from math import *


dessin = svgwrite.Drawing("exercice_carre_rot.svg", size=(800, 600))


def rotation10(angle):
    return (cos(angle), sin(angle))


def rotation01(angle):
    return (sin(angle), cos(angle))


def translater(input, vectTrans):
    x, y = input
    tx, ty = vectTrans
    return (x + tx, y + ty)


def rotation(point, angle):
    x, y = point
    v1x, v1y = rotation10(angle)
    v2x, v2y = rotation01(angle)

    out = (x * v1x - y * v1y, x * v2x + y * v2y)
    return out


# Définition des sommets du carré
carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
# Angle de rotation
angle = pi / 12

# Appliquer la rotation et la translation à chaque sommet
carre_rot = [translater(rotation(sommet, pi / 12), sommet) for sommet in carre]

dessin.add(dessin.polygon(carre_rot, fill="#FF0000", stroke="#000000", opacity=0.7))
dessin.save()
