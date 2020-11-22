#!/usr/bin/env python

import json
from get import path

def get_dict(fn):
    with open (fn) as fin:
        read_data = fin.read()

    start = read_data.index("{'METRICS_S3_BUCKET")
    finish = start + 2000
    finish = start + read_data[start : finish].index('}') + 1
    race_params = read_data[start : finish]
    race_params = race_params.replace('\n','').replace(' ','')
    race_params = race_params.replace("'",'"')
    race_params = json.loads(race_params)
    return race_params
