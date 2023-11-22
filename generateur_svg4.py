#!/usr/bin/env python
import svgwrite
from math import *


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


def prodMatVect(Mat, Vect):
    x, y = Vect
    ((a11, a12), (a21, a22)) = Mat

    x2 = a11 * x + a12 * y
    y2 = a21 * x + a22 * y

    return (x2, y2)


def Matrotation(angle):
    return ((cos(angle), -sin(angle)), (sin(angle), cos(angle)))


dessin = svgwrite.Drawing("exercice_carre_Matrotation.svg", size=(800, 600))

# Définition des sommets du carré
carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
# Angle de rotation
trans = (200, 200)
angle = pi / 12

matRot = Matrotation(angle)

carre_out = [translater(prodMatVect(matRot, sommet), trans) for sommet in carre]

dessin.add(dessin.polygon(carre_out, fill="#FF0000", stroke="#000000", opacity=0.7))
dessin.save()
