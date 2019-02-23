import sys # system
import os # operation system
import psycopg2
import pprint
import numpy as np
from sympy import *
from bokeh.io import output_notebook, push_notebook, show
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.models import GMapPlot, GMapOptions, Circle, Range1d
from bokeh.models import BoxZoomTool, ResetTool, HoverTool
from bokeh.models import CustomJS, Slider
from bokeh.models import TextInput
from bokeh.layouts import row, column, gridplot
from random import random

connection = psycopg2.connect (database = "postgres", user = "postgres", password = "will0723", 
                               host = "127.0.0.1", port = "5432")

cursor = connection.cursor()
cursor.execute ('''SELECT * FROM nba_reference_data.team_advanced_statistics''')
rows = cursor.fetchall()
tspct = [row[1] for row in rows]
efgpct = [row[2] for row in rows]
threepar = [row[3] for row in rows]
ftr = [row[4] for row in rows]
orbpct = [row[5] for row in rows]
drbpct = [row[6] for row in rows]
trbpct = [row[7] for row in rows]
astpct = [row[8] for row in rows]
stlpct = [row[9] for row in rows]
blkpct = [row[10] for row in rows]
tovpct = [row[11] for row in rows]
ortg = [row[12] for row in rows]
drtg = [row[13] for row in rows]
result = [1 if row[14] == "W" else 0 for row in rows]

# # PRINT
# pp = pprint.PrettyPrinter(indent = 4)
# pp.pprint(result)



########################################
X = np.linspace(0, 10)
f = lambda x: x #y=x
F = np.vectorize(f)
Y = F(X)

#random data by F(X) + random residual(upper bound=2)
num = 15 #number of data
random_sign = np.vectorize(lambda x: x if np.random.sample() > 0.5 else -x)
data_X = {
    "tspct": tspct,
    "efgpct": efgpct,
    "threepar": threepar,
    "ftr": ftr,
    "orbpct": orbpct,
    "drbpct": drbpct, 
    "trbpct": trbpct,
    "astpct": astpct, 
    "stlpct": stlpct,
    "blkpct": blkpct,
    "tovpct": tovpct,
    "ortg": ortg,
    "drtg": drtg,
}
data_Y = result

# LINEAR REGRESSION
def linear_regression(X, Y):
    a, b = symbols('a b')
    residual = 0
    for i in range(num):
        residual += (Y[i] - (a * X[i] + b)) ** 2
    # print expand(residual)
    f1 = diff(residual, a)
    f2 = diff(residual, b)
    # print f1
    # print f2
    res = solve([f1, f2], [a, b])
    return res[a], res[b]

LR_X = data_X
LR_Y = []
for key, subDataX in data_X.items(): 
    print(key)
    a, b = linear_regression(subDataX, data_Y)
    h = lambda x: a*x + b
    H = np.vectorize(h)
    source_list = H(subDataX)
    processed_list = [round(i, 3) for i in source_list]
    LR_Y.append(processed_list)

p = figure(plot_width = 400, plot_height = 400)
p.line (LR_X["tspct"], LR_Y[0], line_width = 4)
show(p)
output_file("figure.html")


# TODO
# MILESTONES
# mergeList (+)
# + with +, - with -
# totalX, totalY

# HOW TO PUSH
# git add .
# git commit -m ".."
# git push