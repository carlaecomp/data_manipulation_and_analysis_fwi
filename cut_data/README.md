# Put the model as a Mamute velocity model input
Scripts to manipulation the data of mamute

## Cut the model

### How to run:
``````
python3 cut_model.py param_cut.txt
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
../data/convert/velocity.bin
../data/convert/velocity_cut.bin
201
201
201
100
100
100
``````