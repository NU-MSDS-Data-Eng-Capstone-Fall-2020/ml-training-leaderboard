import json
import boto3

#assuming table name is SpeedRacer

dynamodb.put_item(TableName='SpeedRacer', 
   Item={"racer_name": "steve_racer",
    "car_name": "steves car",
    "model_name": "no name",
    "steering_angle_count": 0,
    "steering_angle_interval": 0.0,
    "speed_cout": 0,
    "speed_interval": 0.0,
    "mono": true,
    "stereo": false,
    "lidar": false,
    "neural_net": "DEEP_CONVOLUTIONAL_NETWORK_SHALLOW",
    "version": 3,
    "batch_size": 32,
    "discount_factor": 0.99,
    "e_greedy_value": 0.90,
    "epsilon_steps": 100,
    "lr": 0.01,
    "num_episodes_between_training": 20,
    "num_epochs": 10,
    "stack_size": 3,
    "term_cond_max_episodes": 1000,
    "track_train": "aragon",
    "episodes_train": 1000,
    "trials_list_train": [list, of, trial, numbers],
    "episodes_list_train": [list, of, episode, numbers],
    "episode_status_train": [list, of, episode, status, values],
    "reward_score_train": [list, of, reward, score, values],
    "elapsed_time_in_milliseconds_train": [list, of, elapsed, time, values],
    "completion_percentage_train": [list, of, completion, percentage, values],
    "total_elapsed_time_train": 40000,
    "avg_pct_completion": 30,
    "trials_list_eval": [list, of, trial, numbers],
    "episodes_list_eval": [list, of, episode, numbers],
    "reset_count_eval": [list, of, reset, count, values],
    "crash_count_eval": [list, of, crash, count, values],
    "off_track_count_eval": [list, of, off, track, count, values],
    "elapsed_time_in_milliseconds_eval": [list, of, elapsed, time, values],
    "completion_percentage_eval": [list, of, completion, percentage, values]})
    
