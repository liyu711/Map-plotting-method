from TranslationMethod import *
import numpy

def filtering_obstacles(obstacles, destination):
		# self adjusting its attempted path according to obstacle
	output_obstacles = obstacles
	point_to_check = destination
	loop_index = 0
	while loop_index < len(output_obstacles):
		check_status = obstacles[loop_index].check_if_point_is_inside_the_obstacle(point_to_check)
		if check_status:
			del output_obstacles[loop_index]
			loop_index -= 1
		loop_index += 1

	return output_obstacles


# def plot_drone(destination, drone):
# 	final_point = destination
# 	ax1.scatter(drone.get_current_point()[0], drone.get_current_point()[1], drone.get_current_point()[1], color='red', marker = 'o')
# 	while drone.get_current_point()[0] != destination[0] and drone.get_current_point()[1] != destination[1]:
# 		for obstacle in list_of_obstacles:
# 			drone.filtering_path(obstacle)
# 	drone.move()
# 	ax1.scatter(drone.get_current_point()[0], drone.get_current_point()[1], get_current_point()[2], color= 'red', marker = 'o')

def get_drone_path(drone, map_to_fly_on, destination, list_of_obstacles):
	flyer = drone
	final_point = destination
	output = [flyer.get_current_point()]

	while flyer.get_current_point()[0] != final_point[0] or flyer.get_current_point()[1] != final_point[1] or flyer.get_current_point()[2] != final_point[2]:
		for obstacle in list_of_obstacles:
			flyer.filtering_path(obstacle)
		flyer.move(final_point)
		output.append(flyer.get_current_point())

	return output


if __name__ == '__main__':
	generator = WorldGenerator()
	map_to_fly_on = generator.generate_map(50, 50, 50, numpy.array([25,25,25]))
	list_of_obstacles = generator.generate_obstacle(20, map_to_fly_on)
	drone = Obstacle(0, numpy.array([0,0,0]))
	destination = numpy.array([25,25,25])

	filtered_obstacles = filtering_obstacles(list_of_obstacles, destination)
	for obstacle in filtered_obstacles:
		print(obstacle.get_current_point())
		print(obstacle.get_side())
	drone_path = get_drone_path(drone, map_to_fly_on, destination, filtered_obstacles)
	print(drone_path)

	with open("drone_path.csv", "w") as drone_output:
		for point in drone_path:
			drone_output_string = str(point[0]) + "," + str(point[1]) + "," + str(point[2]) + "\n"
			drone_output.write(drone_output_string)

	with open("obstacles.csv", "w") as obstacles_output:
		for obstacle in filtered_obstacles:
			obstacle_output_string = str(obstacle.get_current_point()[0]) + "," + str(obstacle.get_current_point()[1]) + "," + str(obstacle.get_current_point()[2]) + "," + str(obstacle.get_side()) + "\n"
			obstacles_output.write(obstacle_output_string)