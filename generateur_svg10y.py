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


aux = 100
points = [(-100, -70), (-100, 0), (-50, 0), (0, -30), (50, 0), (100, 0), (100, -70), (0, 50)]
triangles = [0, 1, 2,2,3,4,4,5,6,1,5,7]

dessin = svgwrite.Drawing("question13.svg", size=(800, 600))

points2 = [
    translater(prodMatVect(Matdilatation(1.2), sommet), (100, 100)) for sommet in points
]




def compose(points, triangles):
    liste_point = []
    colors = ("blue", "red", "green", "purple", "yellow", "white", "coral", "darkblue")
    for i in range(0, len(triangles) // 3):
        print(triangles[3 * i], triangles[3 * i + 1], triangles[3 * i + 2])
        dessin.add(
            dessin.polygon(
                (
                    points[triangles[3 * i]],
                    points[triangles[3 * i + 1]],
                    points[triangles[3 * i + 2]],
                ),
                fill=colors[i%len(colors)],
                opacity=0.5,
                stroke="black",
            )
        )
        
for i in range(1,6):
    MatFinal = prodMatMat(Matrotation((pi/12)*i), Matdilatation(1/i))
    point2_chat = [translater(prodMatVect(MatFinal, sommet), (100*i,0)) for sommet in points]
    compose(point2_chat, triangles)
dessin.save()
