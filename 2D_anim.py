##################
# 2D Random Walk #
##################
 
import random
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#import matplotlib
#from matplotlib.patches import Circle, Wedge, Polygon
#from matplotlib.collections import PatchCollection
 
data = np.loadtxt("all_paths.txt")

x_starts  = data[:,0]
y_starts  = data[:,1]
x_ends    = data[:,2]
y_ends    = data[:,3]
materials = data[:,4]


def map_material(i):
    if i == 0:
        return '#00BBEE' # Moderator
    if i == 1:
        return '#B2C5CB' # Cladding
    if i == 2:
        return '#FFFFFF' # Gap
    if i == 4:
        return '#C7D316' # Fuel
    else:
        return '#000000' # other?

iteration = 0

def plot_single_path(i):
    global iteration
    #if iteration >= x_starts.size :
    if iteration >= 20 :
        return False
    x_vec = [x_starts[iteration], x_ends[iteration]]
    y_vec = [y_starts[iteration], y_ends[iteration]]
    color = map_material(materials[iteration])
    dx = x_ends[iteration] - x_starts[iteration]
    dy = y_ends[iteration] - y_starts[iteration]
    arrow = plt.arrow(x_starts[iteration], y_starts[iteration], dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')
    plt.pause(0.5)
    arrow.remove()
    #plt.pause(0.1)
    #ax.clear()
    #ax.set_aspect('equal')
    #ax.set_ylim(-1.26/2.0, 1.26/2.0)
    #ax.set_xlim(-1.26/2.0, 1.26/2.0)
    #circ=plt.Circle((0,0), radius=0.4750, color='k', fill=False)
    #ax.add_patch(circ)
    #circ=plt.Circle((0,0), radius=0.4180, color='k', fill=False)
    #ax.add_patch(circ)
    #circ=plt.Circle((0,0), radius=0.4096, color='k', fill=False)
    #ax.add_patch(circ)
    plt.plot(x_vec, y_vec, c = color )
    #ax.lines[iteration-1].remove()
    iteration += 1

#xposition = [0]
#yposition = [0]
# 
#def random_walk(i):
#    polar_angle = random.random()*2*math.pi
#    radius      = random.random()
# 
#    xposition.append( xposition[-1] + radius*math.cos(polar_angle) )
#    yposition.append( yposition[-1] + radius*math.sin(polar_angle) )
# 
#    plt.plot( xposition, yposition, c = 'k')

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_ylim(-1.26/2.0, 1.26/2.0)
ax.set_xlim(-1.26/2.0, 1.26/2.0)
circ=plt.Circle((0,0), radius=0.4750, color='k', fill=False)
ax.add_patch(circ)
circ=plt.Circle((0,0), radius=0.4180, color='k', fill=False)
ax.add_patch(circ)
circ=plt.Circle((0,0), radius=0.4096, color='k', fill=False)
ax.add_patch(circ)
 
animation = animation.FuncAnimation( fig, func = plot_single_path, interval = 100 )
plt.show()
