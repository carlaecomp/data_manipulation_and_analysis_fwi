import sys
import numpy as np
import matplotlib.pyplot as plt

# Read the param file
param_file_name = sys.argv[1:][0]
param_file = open(param_file_name, 'r+b')
[file_initial, file_final, type_data, nz_initial, ny_initial, nx_initial, nz_final, ny_final, nx_final] = param_file.readlines()
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
type_data = type_data.decode('utf-8').split()[0]

# Open initial model
with open(file_initial, 'rb') as fid:
    # The model is read like a vector
    if type_data == 'float':
        data = np.fromfile(fid, np.float32)
    elif type_data == "double":
        data = np.fromfile(fid, np.float64)
    else:
        print("Wrong Type")
        exit()

# # Change the initial model, vector to matrix
data = data.reshape((nz_initial,nx_initial,ny_initial))

data = data[0:nz_final, 0:nx_final, 0:ny_final]

# print(ny_final)

grid = data[0]
# grid = np.transpose(grid)
plt.imshow(grid, aspect='auto')
plt.colorbar()
plt.tight_layout()
plt.show()

data = data.flatten('C')

print(data)
print(len(data))

# Save the final model
velocity_model = open(file_final, 'w+b')
velocity_model.write(data)

