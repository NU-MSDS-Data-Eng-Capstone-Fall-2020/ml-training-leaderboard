#!/usr/bin/env python

import json
from collections import OrderedDict 

fn = r'model_metadata.json'

def load(fn):
    with open(fn) as fin:
        return(json.load(fin))

model_metadata = load(fn)

def action_space(model_metadata=model_metadata):
    steer_list = []
    speed_list = []
    for i in model_metadata['action_space']:
        steer_list.append(i['steering_angle'])
        speed_list.append(i['speed'])
    speed_count = len(set(speed_list))
    steer_count = len(set(steer_list))
    speed_max = max(speed_list)
    steer_max = max(steer_list)
    
    return speed_count, speed_max, steer_count, steer_max

def sensors(model_metadata=model_metadata):
    if 'SECTOR_LIDAR' in model_metadata['sensor']:
        lidar = 1
    if 'STEREO_CAMERAS' in model_metadata['sensor']:
        camera = 1
    elif 'STEREO_CAMERAS' not in model_metadata['sensor']:
        camera = 0
    return lidar, camera

def model_dict():
    model_data = OrderedDict()
    speed_count, speed_max, steer_count, steer_max = action_space()
    lidar, camera = sensors()
    model_data['speed_granularity'] = speed_count
    model_data['speed_max'] = speed_max
    model_data['steer_granularity'] = steer_count
    model_data['steer_max'] = steer_count
    model_data['lidar'] = lidar
    model_data['camera'] = camera
    return model_data

