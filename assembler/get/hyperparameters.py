#!/usr/bin/env python

import json
from get import path

# fn = 'training-20201120191008-zXDFsVSeQd2raLaDn-qgHw-robomaker.log'
# fn = 'evaluation-20201120192312-zORIzXAWSCq3YvAyajkrPA-robomaker.log'
# fn = 'leaderboard-20201120195415-Yv9spFcSTlGFM_PsC_5wBg-robomaker.log'

def get_dict(fn):
    with open (fn) as fin:
        read_data = fin.read()

    start = read_data.index('following hyper-parameters')
    finish = start + 600
    start = start + read_data[start : finish].index('{')
    finish = start + read_data[start:finish].index('}') + 1
    hyperparameters = read_data[start : finish]
    hyperparameters = hyperparameters.replace('\n','').replace(' ','')
    hyperparameters = json.loads(hyperparameters)
    return hyperparameters
