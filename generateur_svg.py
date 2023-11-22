#!/usr/bin/env python
import svgwrite

dessin = svgwrite.Drawing("exercice_2.svg", size=(800, 600))
# triangle = [(0, 400), (400, 400), (200, 0)]

carre = [(-100, -100), (100, -100), (100, 100), (-100, 100)]


dessin.add(dessin.polygon(carre, fill="#00FF00", stroke="#000000", opacity=0.7))
dessin.save()
