import numpy
from multiprocessing import Process
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import axes3d


def print_something(number):
	ax.plot(number, number, number)

def do_something():
	print("ouch")

if __name__ == '__main__':
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	p_print = Process(target = print_something, args = (1,))
	p_do = Process(target = do_something, args = ())

	p_do.start()
	p_print.start()
