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


def prodMatMat(MatA, MatB):
    ((a11, a12), (a21, a22)) = MatA
    ((B11, B12), (B21, B22)) = MatB

    return (
        (a11 * B11 + a12 * B21, a11 * B12 + a12 * B22),
        (a21 * B11 + a22 * B21, a21 * B12 + a22 * B22),
    )


dessin = svgwrite.Drawing("question6.svg", size=(800, 600))

# for i in range(1, 10):
#     carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
#     trans = (100 * i, 0)
#     angle = radians(15 * i)
#     dessin.save()
#     carre_out = [
#         translater(prodMatVect(Matrotation(angle), sommet), trans) for sommet in carre
#     ]
#     dessin.add(dessin.polygon(carre_out, fill="#FF0000", stroke="#000000", opacity=0.7))
# dessin.save()


for i in range(1, 10):
    carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]
    trans = (100 * i, 0)
    angle = radians(15 * i)
    dessin.save()
    matModelisation = prodMatMat(Matrotation(angle), Matdilatation(1 / i))
    carre_out = [
        translater(prodMatVect(matModelisation, sommet), trans) for sommet in carre
    ]
    dessin.add(dessin.polygon(carre_out, fill="#FF0000", stroke="#000000", opacity=0.7))
dessin.save()
