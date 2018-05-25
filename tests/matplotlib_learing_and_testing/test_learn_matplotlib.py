import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import axes3d
import numpy
import csv
import datetime as dt
import time
import urllib
import matplotlib.animation as animation
from matplotlib import style
import multiprocessing

# load local file with csv
# with open('example.txt', 'r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter = ',')
# 	for row in plots:
# 		x.append(int(row[0]))
# 		y.append(int(row[1]))


# load local file with numpy
# numpy.loadtxt('example.txt', dlimiter=',', unpack = True)
# only work with 2 variables?


# population_ages = [22, 55,61, 78, 85, 97, 23,84, 123, 94,26,28,76,43,9,8,48,32]
# # ids = [x for x in range(len(population_ages))]
# bins = [0,10,20,30,40,50,60,70,80,90,100,120,130]
# plt.hist(population_ages, bins, histtype ='bar', rwidth = 0.8)
# histogram


# scatter
# plt.scatter(x,y, color = 'color',  marker ='o', s= )


# stackgraph
# (label = 'somegthing', linewidth = 5)

# def graph_data(stock):
# 	stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
# 	source_code = urllib.request.urlopen(stock_price_url).read().decode()
# 	stock_data = []
# 	split_source = source_code.split('\n')
# 	date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter =',', unpack = True)


# # unix time to date time
# example = time.time()
# # a unix time
# actual_time = dt.datetime.fromtimestamp(example)
# # function to convert
# numpy_time = numpy.vectorize(actual_time)
# print(numpy_time)


# 3d graphing
# prepare some coordinates
x, y, z = numpy.indices((1000, 1000, 1000))

# draw cuboids in the top left and bottom right corners, and a link between them
cube1 = (x > 2) & (x < 4) & (y < 4) &( y > 2) & (z > 3) & (z < 5)


# combine the objects into a single boolean array
voxels = cube1 | cube2

# set the colors of each object
colors = numpy.empty(voxels.shape, dtype=object)
colors[cube1] = 'blue'

# and plot everything
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()