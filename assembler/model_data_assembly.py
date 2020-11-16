#!/usr/bin/env python

import json
import yaml
from collections import OrderedDict 

from load_model_data import model_dict
from load_training_lists import training_data
from load_evaluation_lists import evaluation_data

def load_json(fn):
    with open(fn) as fin:
        return(json.load(fin))

def load_yml(fn):
    with open(fn) as fin:
        return(yaml.full_load(fin))

def make_dict():
    model_data = model_dict()

    hyperparameters = load_json(r'hyperparameters.json')
    for i in hyperparameters:
        model_data[i] = hyperparameters[i]

    training_parameters = load_yml(r'training_params.yaml')
    model_data["car_name_train"] = training_parameters["CAR_NAME"]
    model_data["track_train"] = training_parameters["WORLD_NAME"] # <— assert valid track
    model_data["episodes_train"] = training_parameters["NUMBER_OF_EPISODES"]

    eval_parameters = load_yml(r'eval_params.yaml')
    # ensure same racer, car, model
    car_same = eval_parameters["CAR_NAME"] = training_parameters["CAR_NAME"]
    # get eval track, episodes
    model_data["model_name_eval"] = eval_parameters["MODEL_NAME"]
    model_data["racer_name_eval"] = eval_parameters["RACER_NAME"]
    model_data["track_eval"] = eval_parameters["WORLD_NAME"] # <— assert valid$

    training_results = training_data()
    for i in training_results.keys():
        model_data[i] = training_results[i]

    evaluation_results = evaluation_data()
    for i in evaluation_results.keys():
        model_data[i] = evaluation_results[i]

    return model_data

if __name__ == '__main__':
    data_dict = make_dict()
    with open('model_data.json', 'w') as fp:
        json.dump(data_dict, fp)
