#!/usr/bin/env python

import json

fn = 'training-20201120183444-zXDFsVSeQd2raLaDn-qgHw.json'

def get_dict(fn=fn):
    with open(fn) as fin:
        read_data = json.load(fin)

    trials_train = []
    episodes_train = []
    episode_statuses_train = []
    completion_pcts_train = []
    reward_scores_train = []
    elapsed_times_train = []
    metric_times_train = []
    train_lists = {}
    for i in read_data['metrics']:
        trials_train.append(i["trial"])
        episodes_train.append(i["episode"])
        episode_statuses_train.append(i["episode_status"])
        completion_pcts_train.append(i["completion_percentage"])
        reward_scores_train.append(i["reward_score"])
        elapsed_times_train.append(i["elapsed_time_in_milliseconds"])
        metric_times_train.append(i["metric_time"])
    train_lists["trials_train"] = trials_train
    train_lists["episodes_train"] = episodes_train
    train_lists["episode_statuses_train"] = episode_statuses_train
    train_lists["completion_pcts_train"] = completion_pcts_train
    train_lists["reward_scores_train"] = reward_scores_train
    train_lists["elapsed_times_train"] = elapsed_times_train
    train_lists["metric_times_train"] = metric_times_train
    return train_lists
