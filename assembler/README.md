todo:

  - [x] insert assembler.sh into Makefile
  - [x] lint, test
  - [x] checks: train = eval track e.g.
  - [x] checks: ensure employing COPY of user's data
  - [x] code to enable user to identify their tar file
  - [x] filter hyperparameters to smaller set
  - [x] ordered dict
  
outline:

  presently works as shell script ./assemble.sh

  model_data_assembly.py
  - [x] copy users tar data, unzip
  - [x] load hyperparameters.json directly wholely; can be more selective.
  - [x] load training_params.yaml and from there selected items.
  - [x] call training_data module
  - [x] call evaluation_data module
