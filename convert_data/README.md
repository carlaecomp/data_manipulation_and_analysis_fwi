# Put the model as a Mamute velocity model input
Scripts to manipulation the data of mamute

## Convert
Script to convert the model zxy to zyx
### How to run:
``````
python3 convert.py data/param.txt
``````

### Format of param.txt
* name of initial file
* name of final file
* nz of the initial velocity model
* ny of the initial velocity model
* nx of the initial velocity model
* new nz to the final velocity model
* new ny to the final velocity model
* new nx to the final velocity model

#### Example of param.txt
``````
data/GdM_C3_fwi.bin
data/velocity_model.bin
283
910
758
201
201
201
``````