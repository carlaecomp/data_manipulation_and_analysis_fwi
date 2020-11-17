import sys
import numpy as np
import matplotlib.pyplot as plt

# Read the param file
param_file_name = sys.argv[1:][0]
param_file = open(param_file_name, 'r+b')
[first_file, second_file, type_data] = param_file.readlines()

# Prepare the params
first_file = first_file[0:len(first_file)-1]
second_file = second_file[0:len(second_file)-1]
type_data = type_data[0:len(type_data)]

first_file = first_file.decode('utf-8')
second_file = second_file.decode('utf-8')
type_data = type_data.decode('utf-8').split()[0]
print(type_data)

# Open initial model
with open(first_file, 'rb') as fid:
    # The model is read like a vector
    if type_data == 'float':
        data1 = np.fromfile(fid, np.float32)
    elif type_data == "double":
        data1 = np.fromfile(fid, np.float64)
    else:
        print("Wrong Type")
        exit()

# Open initial model
with open(second_file, 'rb') as fid:
    # The model is read like a vector
    if type_data == 'float':
        data2 = np.fromfile(fid, np.float32)
    elif type_data == "double":
        data2 = np.fromfile(fid, np.float64)
    else:
        print("Wrong Type")
        exit()

dataequal = True
if len(data1) == len(data2):
    for i in range(0,len(data2)):
        if data1[i] != data2[i]:
            print("Different")
            dataequal = False
            break
else:
    dataequal = False
    print("Different")

if dataequal:
    print("Equal")

    data1 = data1.reshape((201,201,201), order='C')
    data2 = data2.reshape((201,201,201), order='C')

    data_temp = data1[0]
    (x, y) = np.meshgrid(np.arange(data_temp.shape[0]), np.arange(data_temp.shape[1]))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,data_temp, rstride=5, cstride=1, cmap='viridis', edgecolor='none')
    ax.view_init(azim=120)
    plt.draw()
    plt.title("DATA 1")
    plt.show()

    data_temp = data2[0]
    (x, y) = np.meshgrid(np.arange(data_temp.shape[0]), np.arange(data_temp.shape[1]))
    ax = plt.axes(projection='3d')
    ax.plot_surface(x,y,data_temp, rstride=5, cstride=1, cmap='viridis', edgecolor='none')
    ax.view_init(azim=120)
    plt.draw()
    plt.title("DATA 1")
    plt.show()