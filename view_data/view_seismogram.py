# Author: Carla Santana, based on the Tiago's script
import sys
import numpy as np
import matplotlib.pyplot as plt

# Read and separe the params
param_file_name = sys.argv[1:][0]
param_file = open(param_file_name, 'r+b')
[file_initial, folder_name, n_src, ns, gxi, gxf] = param_file.readlines()
folder_name = folder_name[0:len(folder_name)-1]
folder_name = folder_name.decode('utf-8')

# Prepare the params
file_initial = file_initial[0:len(file_initial)-1]
n_src = int(n_src)
ns = int(ns)
gxi = int(gxi)
gxf = int(gxf)
n = int((gxf-gxi)/2 + 1)

# Open initial model
with open(file_initial, 'rb') as fid:
    # The model is read like a vector 
    # np.float64 is the type double 
    data = np.fromfile(fid, np.float64)

print(len(data))

# Change the vector to a 4D matrix
data = data.reshape(n_src, n, n, ns)

# Select just a sismo from each shot
for i in range(n_src):
    grid = data[i][0]
    grid = np.transpose(grid)
    plt.imshow(grid, cmap='gray',aspect='auto')
    plt.colorbar()
    plt.tight_layout()
    name_file = folder_name+"seismogram_" + str(i) + ".png"
    plt.savefig(name_file, format='png')
    plt.clf()