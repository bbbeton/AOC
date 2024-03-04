import numpy as np 
import scipy as linalg

with open('aoc47-48.txt') as file_input:
    file = file_input.read().splitlines()


#def get_data(char): 
positions = []
velocities = []

for i in range(len(file)):
    line = file[i].replace(' ','').split('@')
    positions.append(line[0].split(','))
    velocities.append(line[1].split(','))
    
print(positions)
print(velocities)

def move(position, velocity):
    for i in range (len(position)):
        position[i] += velocity[i]
    return position

def check_collision(curr_position1, curr_position2, past_position1, past_position2):

 