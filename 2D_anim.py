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
 
data = np.loadtxt("1")

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
alternator = 0
arrow = 0

def plot_single_path(i):
    global iteration
    global arrow
    global alternator
    #if iteration >= 50 :
    print("plotting iteration ", iteration, " out of ", x_starts.size)
    if iteration >= x_starts.size :
        return False
    x_vec = [x_starts[iteration], x_ends[iteration]]
    y_vec = [y_starts[iteration], y_ends[iteration]]
    color = map_material(materials[iteration])
    dx = x_ends[iteration] - x_starts[iteration]
    dy = y_ends[iteration] - y_starts[iteration]
    if alternator == 0 :
        arrow = plt.arrow(x_starts[iteration], y_starts[iteration], dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')
        alternator = 1
    else :
        arrow.remove()
        if iteration > 2 :
            delta_x = x_starts[iteration+1] - x_ends[iteration]
            delta_y = y_starts[iteration+1] - y_ends[iteration]
            if delta_x > 0.001 or delta_y > 0.001:
                dx = x_ends[iteration] - x_starts[iteration]
                dy = y_ends[iteration] - y_starts[iteration]
                arrow2 = plt.arrow(x_starts[iteration], y_starts[iteration], dx, dy, head_width=0.05, head_length=0.1, fc='k', ec='k')
        plt.plot(x_vec, y_vec, c = color )
        iteration += 1
        alternator = 0
    #plt.pause(0.5)
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
    #plt.pause(0.5)
    #ax.lines[iteration-1].remove()

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

Writer = animation.writers['ffmpeg']
writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=10000)
 
#animation = animation.FuncAnimation( fig, func = plot_single_path, x_starts.size, interval = 500 )
animation = animation.FuncAnimation( fig, plot_single_path, x_starts.size*2, interval = 500 )
plt.show()
#animation.save('test.mp4', writer=writer, dpi=300)
