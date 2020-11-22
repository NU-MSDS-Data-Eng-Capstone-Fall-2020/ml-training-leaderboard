#!/usr/bin/env python

import json
from collections import OrderedDict

def get_dict(fn):
    
    with open(fn) as fin:
        read_data = json.load(fin)
        
    metric_times_train = []
    trials_train = []
    episode_statuses_train = []
    reward_scores_train = []
    completion_pcts_train = []
    elapsed_times_train = []
    episodes_train = []
    train_lists = OrderedDict()
    
    for i in read_data['metrics']:
        metric_times_train.append(i["metric_time"])
        trials_train.append(i["trial"])
        episode_statuses_train.append(i["episode_status"])
        reward_scores_train.append(i["reward_score"])
        completion_pcts_train.append(i["completion_percentage"])
        elapsed_times_train.append(i["elapsed_time_in_milliseconds"])
        episodes_train.append(i["episode"])
    
    train_lists["trials_train"] = trials_train
    train_lists["episodes_train"] = episodes_train
    train_lists["episode_statuses_train"] = episode_statuses_train
    train_lists["completion_pcts_train"] = completion_pcts_train
    train_lists["reward_scores_train"] = reward_scores_train
    train_lists["elapsed_times_train"] = elapsed_times_train
    train_lists["metric_times_train"] = metric_times_train
    return train_lists
