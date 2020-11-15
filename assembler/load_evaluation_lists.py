#!/usr/bin/env python

import json

fn = r'evaluation.json'

def load_json(fn):
    with open(fn) as fin:
        return(json.load(fin))

data = load_json(fn)

def evaluation_data(data=data):
    trials = []
    episode_statuses = []
    completion_pcts = []
    reset_counts = []
    crash_counts = []
    off_track_counts = []
    elapsed_times = []
    metric_times = []
    evaluation_lists = {}
    for i in data['metrics']:
        trials.append(i["trial"])
        episode_statuses.append(i["episode_status"])
        completion_pcts.append(i["completion_percentage"])
        reset_counts.append(i["reset_count"])
        crash_counts.append(i["crash_count"])
        off_track_counts.append(i["off_track_count"])
        elapsed_times.append(i["elapsed_time_in_milliseconds"])
        metric_times.append(i["metric_time"])
    evaluation_lists["trials"] = trials
    evaluation_lists["episode_statuses"] = episode_statuses
    evaluation_lists["completion_pcts"] = completion_pcts
    evaluation_lists["reset_counts"] = reset_counts
    evaluation_lists["crash_counts"] = crash_counts
    evaluation_lists["off_track_counts"] = off_track_counts
    evaluation_lists["elapsed_times"] = elapsed_times
    evaluation_lists["metric_times"] = metric_times 
    return evaluation_lists
