#!/usr/bin/env python

import json

fn = r'evaluation.json'

def load_json(fn):
    with open(fn) as fin:
        return(json.load(fin))

data = load_json(fn)

def evaluation_data(data=data):
    trials_eval = []
    episode_statuses_eval = []
    completion_pcts_eval = []
    reset_counts_eval = []
    crash_counts_eval = []
    off_track_counts_eval = []
    elapsed_times_eval = []
    metric_times_eval = []
    evaluation_lists = {}
    for i in data['metrics']:
        trials_eval.append(i["trial"])
        episode_statuses_eval.append(i["episode_status"])
        completion_pcts_eval.append(i["completion_percentage"])
        reset_counts_eval.append(i["reset_count"])
        crash_counts_eval.append(i["crash_count"])
        off_track_counts_eval.append(i["off_track_count"])
        elapsed_times_eval.append(i["elapsed_time_in_milliseconds"])
        metric_times_eval.append(i["metric_time"])
    evaluation_lists["trials_eval"] = trials_eval
    evaluation_lists["episode_statuses_eval"] = episode_statuses_eval
    evaluation_lists["completion_pcts_eval"] = completion_pcts_eval
    evaluation_lists["reset_counts_eval"] = reset_counts_eval
    evaluation_lists["crash_counts_eval"] = crash_counts_eval
    evaluation_lists["off_track_counts_eval"] = off_track_counts_eval
    evaluation_lists["elapsed_times_eval"] = elapsed_times_eval
    evaluation_lists["metric_times_eval"] = metric_times_eval
    return evaluation_lists
