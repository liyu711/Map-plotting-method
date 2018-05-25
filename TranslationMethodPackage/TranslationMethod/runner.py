from TranslationMethod import *
import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import multiprocessing
from multiprocessing import Process


generator = WorldGenerator()
map_to_fly_on = generator.generate_map(50, 50, 50, numpy.array([25,25,0]))
list_of_obstacles = generator.generate_obstacle(10, map_to_fly_on)
manager = multiprocessing.Manager()
drone_points = []
drone_points = manager.list()
fig = plt.figure()
ax1 = axes3d.Axes3D(fig)

def plot_obstacles():
	voxels = list_of_obstacles[0].get_cubic_value_for_plotting(map_to_fly_on)
	for obstacle in list_of_obstacles:
		voxel = obstacle.get_cubic_value_for_plotting(map_to_fly_on)
		voxels = voxels | voxel
		print(obstacle.center)
		print(obstacle.side_length)

	fig = plt.figure()
	ax1 = axes3d.Axes3D(fig)
	ax1.voxels(voxels, facecolor = 'blue')

def plot_drone(destination):
	drone = Obstacle(0, numpy.array([0,0,0]))
	print(drone.get_current_point()[0])
	final_point = destination
	ax1.scatter(drone.get_current_point()[0], drone.get_current_point()[1], drone.get_current_point()[1], color='red', marker = 'o')
	while drone.get_current_point()[0] != destination[0] and drone.get_current_point()[1] != destination[1]:
		for obstacle in list_of_obstacles:
			drone.filtering_path(obstacle)
	drone.move()
	ax1.scatter(drone.get_current_point()[0], drone.get_current_point()[1], get_current_point()[2], color= 'red', marker = 'o')

p_plot_obstacles = Process(target = plot_obstacles, args=())
p_plot_drone = Process(target = plot_drone, args = (numpy.array([25,25,0])))

p_plot_obstacles.start()
p_plot_drone.start()
p_plot_obstacles.join()
p_plot_drone.join()
plt.show()

