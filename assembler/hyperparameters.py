#!/usr/bin/env python

import json

# copy training-20201120191007-zXDFsVSeQd2raLaDn-qgHw-sagemaker.log to temp.log

def get_dict(training_log_file):
    with open ('s.log') as f:
        read_data = f.read()

    start = read_data.index('following hyper-parameters')
    finish = start + 600
    start = start + read_data[start : finish].index('{')
    finish = start + read_data[start:finish].index('}') + 1
    hyperparameters = read_data[start : finish]
    hyperparameters = hyperparameters.replace('\n','').replace(' ','')
    hyperparameters = json.loads(hyperparameters)
    return hyperparameters
