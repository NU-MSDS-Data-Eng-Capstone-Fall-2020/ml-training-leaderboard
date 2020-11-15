#!/usr/bin/env python

import json

fn = r'training.json'

def load_json(fn):
    with open(fn) as fin:
        return(json.load(fin))

data = load_json(fn)

def training_data(data=data):
    trials = []
    episodes = []
    episode_statuses = []
    completion_pcts = []
    reward_scores = []
    elapsed_times = []
    metric_times = []
    train_lists = {}
    for i in data['metrics']:
        trials.append(i["trial"])
        episodes.append(i["episode"])
        episode_statuses.append(i["episode_status"])
        completion_pcts.append(i["completion_percentage"])
        reward_scores.append(i["reward_score"])
        elapsed_times.append(i["elapsed_time_in_milliseconds"])
        metric_times.append(i["metric_time"])
    train_lists["trials"] = trials
    train_lists["episodes"] = episodes
    train_lists["episode_statuses"] = episode_statuses
    train_lists["completion_pcts"] = completion_pcts
    train_lists["reward_scores"] = reward_scores
    train_lists["elapsed_times"] = elapsed_times
    train_lists["metric_times"] = metric_times 
    return train_lists
