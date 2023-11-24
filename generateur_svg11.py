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







def prodMatVect3D(Mat, Vect ):
    x, y,z = Vect
    ( (a11,a12,a13), (a21, a22,a23), (a31, a32,a33) ) = Mat

    x2 = a11 * x + a12 * y+ a13 * z
    y2 = a21 * x + a22 * y+ a23 * z
    z2 = a31 * x + a32 * y+ a33 * z

    return (x2,y2,z2)

def prodMatMat3D(MatA, MatB ):

    ( (a11,a12,a13),
    (a21, a22,a23),
    (a31, a32,a33) )  = MatA

    ( (b11,b12,b13),
    (b21, b22,b23),
    (b31, b32,b33) )  = MatB

    return ( (a11*b11+a12* b21+a13*b31 , a11*b12+a12* b22+a13*b32,a11*b13+a12* b23+a13*b33  ),
     (  a21*b11+a22* b21+ a23*b31, a21*b12+a22* b22 +a23*b32,  a21*b13+a22* b23+a23*b33),
     (  a31*b11+a32* b21+ a33*b31, a31*b12+a32* b22 +a33*b32,  a31*b13+a32* b23+a33*b33))

def Matdilatation3D(coefDilatation):
         return ((coefDilatation,0,0), (0,coefDilatation,0), (0,0,coefDilatation))

def Matrotation3DY(angle):
     return (
            (cos(angle), 0,sin(angle)),
            (0,1,0,),
            (-sin(angle),0, cos(angle)))

def Matrotation3DX(angle):
     return (
            (1, 0,0),
            (0, cos(angle),-sin(angle)),
            (0,sin(angle), cos(angle)))

def Matrotation3DZ(angle):
        return (
                (cos(angle), -sin(angle),0),
                (sin(angle), cos(angle),0),
                (0,0,1))



dessin = svgwrite.Drawing("question17.svg", size=(800, 600))

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
                fill=colors[(i%(len(colors)*2))//2],
                opacity=0.5,
                stroke="black",
            )
        )
        

aux=100
#définir le cube : 6 faces, chacune composée de 4 sommets. Définissez 6 variables : face1, face2, etc. 
points=[[-aux, -aux, aux], #point 0 (face devant)
        [-aux, aux, aux],#point 1   (face devant)
        [aux, aux, aux],#point 2    (face devant)
        [aux, -aux, aux],#point 3   (face devant)
        [-aux, -aux, -aux],#point 4 (face arrière)
        [-aux, aux, -aux],#point 5  (face arrière)
        [aux, aux, -aux],#point 6   (face arrière)
        [aux, -aux, -aux]
        ]#point 7 (face arrière)
        
cube=[0,1,2,   #triangle 1 face 1 (devant)
    0,2,3,     #triangle 2 face 1
    4,5,6,     #triangle 1 face 2 (arriere)
    4,6,7,     #triangle 2 face 2
    0,1,5,     #triangle 1 face 3 (gauche)
    0,5,4,     #triangle 2 face 3
    3,2,6,     #triangle 1 face 4 (droite)
    3,6,7,     #triangle 2 face 4
    1,2,6,     #triangle 1 face 5 (dessus)
    1,6,5,     #triangle 2 face 5
    0,3,7,     #triangle 1 face 6 (dessous)
    0,7,4]     #triangle 2 face 6

def projection(point3d):
    return((point3d[0],point3d[1]))

def changez_mon_nom(point, direction):
    x, y, z = point
    dx, dy, dz = direction
    return (x + dx, y + dy, z + dz)



points_proj = [ projection(sommet) for sommet in points ]
print(points_proj)
points_proj2 = [changez_mon_nom(sommet, (0, 0, 0))[:2] for sommet in points]
print(points_proj2)

for i in range(1,10):
    MatFinal = prodMatMat3D(prodMatMat3D(prodMatMat3D(Matdilatation3D(1/i),Matrotation3DY(radians(15*i))),Matrotation3DX(radians(-25*i))),Matrotation3DZ(radians(5*i)))
    point2 = [
        translater(prodMatVect3D(MatFinal, sommet)[:2], (100*i, 0)) for sommet in points
    ]
    compose(point2, cube)

dessin.save()
