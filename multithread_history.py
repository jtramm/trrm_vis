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
 
r1 = np.loadtxt("r1.txt")
r2 = np.loadtxt("r2.txt")
r3 = np.loadtxt("r3.txt")
r4 = np.loadtxt("r4.txt")
n_rays = 4
sz1 = r1[:,0].size
sz2 = r2[:,0].size
sz3 = r3[:,0].size
sz4 = r4[:,0].size
max_iters = max([sz1, sz2, sz3, sz4])
print("maximum iters = ", max_iters)

rays = [r1, r2, r3, r4]

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
arrows = [0,0,0,0]
alternator = 0
begin = 0
begin_frames = 5
ray_colors = ['k', 'r', 'g', 'b']

def plot_single_path(i):
    global iteration
    global arrows
    global alternator
    global begin
    global begin_frames
    global ray_colors
    if begin < begin_frames:
        begin += 1
    else:
        if iteration >= max_iters :
            return False
        print("plotting iteration ", iteration, " out of ", max_iters)

        for r in range(n_rays):
            data = rays[r]
            x_starts  = data[:,0]
            y_starts  = data[:,1]
            x_ends    = data[:,2]
            y_ends    = data[:,3]
            materials = data[:,4]
            if iteration < x_starts.size:
                x_vec = [x_starts[iteration], x_ends[iteration]]
                y_vec = [y_starts[iteration], y_ends[iteration]]
                color = map_material(materials[iteration])
                dx = x_ends[iteration] - x_starts[iteration]
                dy = y_ends[iteration] - y_starts[iteration]
                if alternator == 0 :
                    arrows[r] = plt.arrow(x_starts[iteration], y_starts[iteration], dx, dy, head_width=0.05, head_length=0.05, fc=ray_colors[r])
                    if iteration > 0 :
                        delta_x = x_starts[iteration] - x_ends[iteration-1]
                        delta_y = y_starts[iteration] - y_ends[iteration-1]
                        if delta_x > 0.001 or delta_y > 0.001:
                            plt.scatter(x_starts[iteration], y_starts[iteration], marker='o', c='k')
                    else:
                            plt.scatter(x_starts[iteration], y_starts[iteration], marker='o', c='k')
                else :
                    if iteration < x_starts.size - 1 :
                        arrows[r].remove()
                        delta_x = x_starts[iteration+1] - x_ends[iteration]
                        delta_y = y_starts[iteration+1] - y_ends[iteration]
                        if delta_x > 0.001 or delta_y > 0.001:
                            dx = x_ends[iteration] - x_starts[iteration]
                            dy = y_ends[iteration] - y_starts[iteration]
                            plt.arrow(x_starts[iteration], y_starts[iteration], dx, dy, head_width=0.05, head_length=0.05, fc=ray_colors[r])
                    plt.plot(x_vec, y_vec, c = color )
        if alternator == 0:
            alternator = 1
        else:
            alternator = 0
            iteration += 1


fig, ax = plt.subplots()
ax.set_yticks(ticks=[])
ax.set_xticks(ticks=[])
ax.set_aspect('equal')
ax.set_ylim(-1.26/2.0, 1.26/2.0)
ax.set_xlim(-1.26/2.0, 1.26/2.0)
circ=plt.Circle((0,0), radius=0.4750, color='k', fill=False)
ax.add_patch(circ)
circ=plt.Circle((0,0), radius=0.4180, color='k', fill=False)
ax.add_patch(circ)
circ=plt.Circle((0,0), radius=0.4096, color='k', fill=False)
ax.add_patch(circ)

# Turn off tick labels

Writer = animation.writers['ffmpeg']
writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=10000)
 
#animation = animation.FuncAnimation( fig, func = plot_single_path, x_starts.size, interval = 500 )
animation = animation.FuncAnimation( fig, plot_single_path, max_iters*2 + begin_frames, interval = 500 )
#plt.show()
animation.save('test.mp4', writer=writer, dpi=300)
