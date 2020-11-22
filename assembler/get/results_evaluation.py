#!/usr/bin/env python

import json
from collections import OrderedDict

def get_dict(fn):

    with open(fn) as fin:
        read_data = json.load(fin)
        
    completion_pcts_eval = []
    off_track_counts_eval = []
    episode_statuses_eval = []
    elapsed_times_eval = []
    metric_times_eval = []
    reset_counts_eval = []
    crash_counts_eval = []
    trials_eval = []
    evaluation_lists = OrderedDict()

    for i in read_data['metrics']:
        completion_pcts_eval.append(i["completion_percentage"])
        off_track_counts_eval.append(i["off_track_count"])
        episode_statuses_eval.append(i["episode_status"])
        elapsed_times_eval.append(i["elapsed_time_in_milliseconds"])
        metric_times_eval.append(i["metric_time"])
        reset_counts_eval.append(i["reset_count"])
        crash_counts_eval.append(i["crash_count"])
        trials_eval.append(i["trial"])

    evaluation_lists["completion_pcts_eval"] = completion_pcts_eval
    evaluation_lists["off_track_counts_eval"] = off_track_counts_eval
    evaluation_lists["episode_statuses_eval"] = episode_statuses_eval
    evaluation_lists["elapsed_times_eval"] = elapsed_times_eval
    evaluation_lists["metric_times_eval"] = metric_times_eval
    evaluation_lists["reset_counts_eval"] = reset_counts_eval
    evaluation_lists["crash_counts_eval"] = crash_counts_eval
    evaluation_lists["trials_eval"] = trials_eval
    return evaluation_lists
