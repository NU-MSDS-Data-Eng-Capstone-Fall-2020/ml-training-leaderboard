#!/usr/bin/env python

import json

# copy leaderboard-20201120195415-Yv9spFcSTlGFM_PsC_5wBg-robomaker.log to temp.log

def get_dict(leaderboard_robomaker_log):
    with open ('temp.log') as f:
        read_data = f.read()

    start = read_data.index("{'METRICS_S3_BUCKET")
    finish = start + 2000
    finish = start + read_data[start : finish].index('}') + 1
    race_params = read_data[start : finish]
    race_params = race_params.replace('\n','').replace(' ','')
    race_params = json.loads(race_params)
    return race_params
