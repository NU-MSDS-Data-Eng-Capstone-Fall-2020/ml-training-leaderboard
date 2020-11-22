#!/usr/bin/env python
# https://wiki.deepracing.io/Customise_Local_Training

import json
from collections import OrderedDict
from get import metadata_model, hyperparameters, metadata_stage, results_evaluation, results_training, path

path_metadata_model = path.finder('model')
path_logs_training, path_training_results = path.finder('training')
path_logs_evaluation, path_evaluation_results = path.finder('evaluation')
path_logs_leaderboard = path.finder('leaderboard')

def make_dict():
    model_data = metadata_model.get_dict(path_metadata_model)
    hyperparameters_dict = hyperparameters.get_dict(path_logs_training)
    for i in hyperparameters_dict:
        model_data[i] = hyperparameters_dict[i]

    metadata_training = metadata_stage.get_dict(path_logs_training)
    model_data["track_train"] = metadata_training["WORLD_NAME"] # <— assert valid track

    metadata_evaluation = metadata_stage.get_dict(path_logs_evaluation)
    # get eval track, episodes
    model_data["model_name_eval"] = metadata_evaluation["MODEL_NAME"]
    model_data["racer_name_eval"] = metadata_evaluation["RACER_NAME"]
    model_data["track_eval"] = metadata_evaluation["WORLD_NAME"] # <— assert valid$
    model_data["trials_eval"] = metadata_evaluation["NUMBER_OF_TRIALS"]
    # ensure race type is time trial and same training and eval
    race_type_same = metadata_evaluation["RACE_TYPE"] == metadata_training["RACE_TYPE"] == "TIME_TRIAL"

    metadata_leaderboard = metadata_stage.get_dict(path_logs_leaderboard)
    model_data["trials_lead"] = int(metadata_leaderboard["NUMBER_OF_TRIALS"])
    model_data["track_lead"] = metadata_leaderboard["WORLD_NAME"] # <— assert valid$
    # ensure model name is same
    model_name_same = metadata_evaluation["MODEL_NAME"] == metadata_leaderboard["MODEL_NAME"]
    # ensure racer name is same
    racer_name_same = metadata_evaluation["RACER_NAME"] == metadata_leaderboard["RACER_NAME"]
    # ensure race type is same
    race_type_same = metadata_leaderboard["RACE_TYPE"] == metadata_training["RACE_TYPE"] == "TIME_TRIAL"

    results_training_dict = results_training.get_dict(path_training_results)
    for i in results_training_dict.keys():
        model_data[i] = results_training_dict[i]

    results_evaluation_dict = results_evaluation.get_dict(path_evaluation_results)
    for i in results_evaluation_dict.keys():
        model_data[i] = results_evaluation_dict[i]

    return model_data

if __name__ == '__main__':
    data_dict = make_dict()
    with open('model_data.json', 'w') as fp:
        json.dump(data_dict, fp)
