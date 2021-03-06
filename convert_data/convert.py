import sys
import numpy as np
import matplotlib.pyplot as plt

# Read the param file
param_file_name = sys.argv[1:][0]
param_file = open(param_file_name, 'r+b')
[file_initial, file_final, nz_initial, ny_initial, nx_initial, nz_final, ny_final, nx_final] = param_file.readlines()

# Prepare the params
file_initial = file_initial[0:len(file_initial)-1]
file_final = file_final[0:len(file_final)-1]
nz_initial = int(nz_initial)
ny_initial = int(ny_initial)
nx_initial = int(nx_initial)
nz_final = int(nz_final)
ny_final = int(ny_final)
nx_final = int(nx_final)

file_initial = file_initial.decode('utf-8')
file_final = file_final.decode('utf-8')

# Open initial model
with open(file_initial, 'rb') as fid:
    # The model is read like a vector
    data = np.fromfile(fid, np.float32)

# # Change the initial model, vector to matrix [Reshape like in Fortran code]
data = data.reshape((nz_initial,nx_initial,ny_initial), order='F')

# Order of the permute
order = [1,2,0]
data = np.transpose(data, order)
data = data[0:nz_final, 0:ny_final, 0:nx_final]

# Change the matrix to vector [Flatten like in C code]
data = data.flatten('C')
data = np.float64(data)
print(len(data))

# Save the final model
velocity_model = open(file_final, 'w+b')
velocity_model.write(data)