#!/usr/bin/env python
import svgwrite


def translater(input, vectTrans):
    x, y = input
    tx, ty = vectTrans
    return (x + tx, y + ty)


dessin = svgwrite.Drawing("exercice_carre_trans.svg", size=(800, 600))

carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]

trans = (200, 200)

carre_trans = [translater(sommet, trans) for sommet in carre]

dessin.add(dessin.polygon(carre_trans, fill="#FF0000", stroke="#000000", opacity=0.7))
dessin.save()
