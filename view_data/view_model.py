# Author: Carla Santana, based on the Tiago's script
import sys
import numpy as np
import matplotlib.pyplot as plt

# Read and separe the params
param_file_name = sys.argv[1:][0]
param_file = open(param_file_name, 'r+b')
[file_initial, folder_name, nz, nx, ny] = param_file.readlines()

# Prepare the params
file_initial = file_initial[0:len(file_initial)-1]
nz = int(nz)
nx = int(nx)
ny = int(ny)
folder_name = folder_name[0:len(folder_name)-1]
folder_name = folder_name.decode('utf-8')

# Open initial model
with open(file_initial, 'rb') as fid:
    # The model is read like a vector 
    # np.float64 is the type double 
    data = np.fromfile(fid, np.float64)

print(len(data))

# Change the vector to a 3D matrix
data = data.reshape(nz, nx, ny)

# Select just a piece from the model to plot
grid = data[0]
grid = np.transpose(grid)
plt.imshow(grid, aspect='auto')
plt.colorbar()
plt.tight_layout()
name_file = str(folder_name)+'model2D.png'
print (name_file)
plt.savefig(name_file, format='png')
plt.clf()

# Plot the data as a 3D Plot
data_temp = data[0]
(x, y) = np.meshgrid(np.arange(data_temp.shape[0]), np.arange(data_temp.shape[1]))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,data_temp, rstride=5, cstride=1, cmap='viridis', edgecolor='none')
ax.view_init(azim=120)
plt.draw()
name_file = folder_name+"model3D.png"
plt.savefig(name_file, format='png')
plt.clf()