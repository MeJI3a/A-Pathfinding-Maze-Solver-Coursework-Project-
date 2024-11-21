#!/usr/bin/env python3.10

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from queue import PriorityQueue
from matplotlib.patches import Rectangle

maze = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
]

'''
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]
'''

start = (0, 0) #row, col
end = (7, 8)   #row, col

wall = 1

#########################################################
plt.ion()
fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1) 
ax_title_text="Maze Solver\nCost of the shortest path:"
ax.set_title(ax_title_text)

maze_max_rows=len(maze)
maze_max_columns=len(maze[0])

plt.ylim(maze_max_rows, 0)
plt.xlim(0, maze_max_columns)



##########################################################   
def get_patches_index(x,y):
    return y * (maze_max_rows) + x



##########################################################   
def draw_maze():
    for r in range(maze_max_rows):
        for c in range(maze_max_columns):
            if (maze[r][c] == 1):
                ax.add_patch( Rectangle((c, r), 1, 1, fc='black', ec ='black', lw = .5))
            else:
                ax.add_patch( Rectangle((c, r), 1, 1, fc='none', ec ='black', lw = .5))
    
    ax.patches[ get_patches_index(start[1],start[0]) ].set_facecolor('yellow')
    ax.patches[ get_patches_index(end[1],end[0]) ].set_facecolor('green')



#############################################################
def set_rectangle_label(x, y, text):
    rx, ry = ax.patches[ get_patches_index(x,y) ].get_xy()
    cx = rx + ax.patches[ get_patches_index(x,y)].get_width()/2.0
    cy = ry + ax.patches[ get_patches_index(x,y)].get_height()/2.0
    ax.annotate(text, (cx, cy), color='red', weight='bold', fontsize=10, ha='center', va='center')



#############################################################
def highlight_rect(x,y, text):
    
    rect = ax.patches[ get_patches_index(x,y) ]
    face_color = rect.get_facecolor()
    
    for i in range(3):
        rect.set_facecolor("blue")
        plt.pause(.01)
        rect.set_facecolor('lightgrey')
        plt.pause(.01)
        
    if  end == (y,x):
        rect.set_facecolor(face_color)
    
    set_rectangle_label(x,y,text)
    

    
#############################################################
def draw_path(path):
    if path:
        for node in path:
            ax.patches[ get_patches_index(node[1],node[0]) ].set_facecolor('blue')
            plt.pause(.02)

##############################################################
### A* algo
##############################################################

# Define possible movements
movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(position, end):
    distance = abs(position[0] - end[0]) + abs(position[1] - end[1])
    highlight_rect(position[1], position[0], str(distance))
    return distance

# Define cost calculation function
def calculate_cost(path):
    # In this simple maze problem, each step has the same cost (1)
    #return len(path) if (path != None) else -1
    return len(path) if (path != None) else -1


###############################################
def is_legal_pos(pos):
    ret = False
    if (pos[0] >= 0)\
        and (pos[0] < maze_max_rows)\
        and (pos[1] >= 0)\
        and (pos[1] < maze_max_columns)\
        and ( maze[pos[0]][pos[1]] != wall ):
        ret = True
    return ret


# A* algorithm to find the shortest path
def astar(maze, start, end):
    queue = PriorityQueue()
    queue.put((0, start, [start]))
    visited = set([start])
    attempts = []  # To track all the nodes that the algorithm examines
    
    while not queue.empty():
        _, position, path = queue.get()
        attempts.append(position)  # Record the node as an attempt
        
        if position == end:
            return path, attempts
        
        for move in movements:
            next_pos = (position[0] + move[0], position[1] + move[1]) 
            if is_legal_pos(next_pos) and (next_pos not in visited):
                new_path = path + [next_pos]
                visited.add(next_pos)
                cost = calculate_cost(new_path) + heuristic(next_pos, end)
                queue.put((cost, next_pos, new_path))
                
    return None, attempts
#############################################################



## Main ###
draw_maze()

# Run A* to find the shortest path and record the attempts
shortest_path, attempts = astar(maze, start, end)

draw_path(shortest_path)

ax_title_text=ax_title_text + str(calculate_cost(shortest_path))
ax.set_title(ax_title_text)

plt.ioff()
plt.show()