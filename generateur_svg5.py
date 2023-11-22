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


def Matdilatation(coefDilatation):
    return ((coefDilatation, 0), (0, coefDilatation))


dessin = svgwrite.Drawing("question3.svg", size=(800, 600))

x_position = 50

# Crée les 4 carrés
for i in range(1, 5):
    # Définition du carré
    carre = [(-50, -50), (50, -50), (50, 50), (-50, 50)]

    # Applique la matrice de dilatation
    matDilatation = Matdilatation(0.5**i)
    carre = [prodMatVect(matDilatation, sommet) for sommet in carre]

    # Applique la translation
    carre = [translater(sommet, (x_position + i * 100, 400)) for sommet in carre]

    # Dessine le carré
    dessin.add(dessin.polygon(carre, fill="#b2b2d5", stroke="#000000", opacity=1 / i))

    # Met à jour la position pour le prochain carré
    x_position += 50

# Sauvegarde le dessin dans un fichier SVG
dessin.save()
