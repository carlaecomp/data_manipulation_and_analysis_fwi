import sys
import numpy as np

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

# Open initial model
with open(file_initial, 'rb') as fid:
    # The model is read like a vector
    model_initial_vector= np.fromfile(fid, np.float32)

# # Change the initial model, vector to matrix
model_initial_matrix = model_initial_vector.reshape((nz_initial,nx_initial,ny_initial))

model_initial_matrix = model_initial_matrix[0:nz_final, 0:nx_final, 0:ny_final]
model_initial_matrix = np.transpose(model_initial_matrix)
model_initial_matrix = model_initial_matrix.flatten('F')
print(len(model_initial_matrix))

# Save the final model
velocity_model = open(file_final, 'w+b')
velocity_model.write(model_initial_matrix)