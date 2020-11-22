## todo:

  - [ ] lint, test
  - [x] checks: train = eval track e.g.
  - [x] code to enable user to identify path to file
  - [ ] filter hyperparameters to smaller set
  - [ ] ensure hyperparameters are the same in training, evaluation, leaderboard log files.
  - [ ] ensure: train = eval track e.g.
  
## outline:

###  model_data_assembly.py
  - [x] import modules that get:
    - [x] metadata of model,
    - [x] hyperparameters of model,
    - [x] metadata from training, evaluation, leaderboard stages, 
    - [x] results from training, evaluation.
  - [x] get paths to 1 model file, 2 training files, 2 evaluation files and 1 leaderboard file.
  - [x] make ordered dict "model_data" from metadata of the model.
  - [x] add hyperparameters to "model_data".
  - [x] add metadata from training stage to "model_data"
  - [x] add metadata from evaluation stage to "model_data"
  - [x] add metadata from leaderboard stage to "model_data"
  - [x] add results from training to "model_data"
  - [x] add results from evaluation to "model_data"
  
  ###  hyperparameters.py and metadata_stage.py
  
  Both modules use similar methods to parse the log files for the hyperparameters and meta data from the training, evaluation and leaderboard stages.  Presently, only use hyperparameters from training stage.  A check should be put in place to ensure all 3 hyperparameters are the same.
  
  ###  path.py
  
  Uses ```tkinter``` package, which is the standard Python interface to the ```Tk``` GUI toolkit, to let the user open a finder window to find and select the entitled files in their file system.  This module ensures the user only selects required file type (```*.log``` or ```*.json``` depending on the situation), ensures that the user selects a ```robomaker.log``` and not ```sagemaker.log``` file, and returns a path to the desired file.  For training, evaluation and leaderboard files, a ```*.log``` file is found by the user and the module uses this path to find a ```.json``` file and that path is returned as well.

### ```results_evaluation.py``` and ```results_training.py```

Both assemble a dictionary of lists from the ```*metrics.json``` files in the ```training``` and ```leaderboard``` folders.

## source file, item, data type (integer if not noted)

model_data.json:
- speed_granularity
- speed_max
- steer_granularity
- steer_max
- lidar
- camera

hyperparameters.json:
- batch_size
- beta_entropy - f
- discount_factor - f
- e_greedy_value - f
- epsilon_steps
- exploration_type - s
- loss_type - s
- lr - f
- num_episodes_between_training
- num_epochs
- stack_size
- term_cond_avg_score - f
- term_cond_max_episodes - f

training_params.yaml (all except episodes_train are string):
- car_name_train
- track_train
- episodes_train

eval_params.yaml (all string):
- model_name_eval
- racer_name_eval
- track_eval

training.json (all list type):
- trials_train
- episode_statuses_train
- completion_pcts_train
- reward_scores_train
- elapsed_times_train
- metric_times_train

evaluation.json (all list type):
- trials_eval
- episode_statuses_eval
- completion_pcts_eval
- reset_counts_eval
- crash_counts_eval
- off_track_counts_eval
- elapsed_times_eval
- metric_times_eval


## Four folders are downloadable from AWS DR: here are their file trees

Logs appear mostly useless, but are only source of hyperparameters.

### One folder with name [your model name]-model is downloadable:

1. MODEL data

[your model name]-model

    agent
        model.pb
    model_metadata.json
        {
        action_space: [
            {
            steering_angle: integer,
            speed: float
            index: integer
            },
            {
            repeat
            }
            repeat...
            ],
        sensor: [ string ]
        neural_network: string
        version: integer
        }
    worker_0.multi_agent_graph_0.json
    worker_0.multi_agent_graph.main_level.main_level.agent_0.csv

### Three folders with identical names [your model name] are downloadable:

2. TRAINING data

[your model name]

    logs
        training
            "training-<14 digit date time>-<22 character URL>-sagemaker.log
            "training-<14 digit date time>-<22 character URL>-robomaker.log
    metrics
        training
            training-<14 digit date time>-<22 character URL>.json
                {metrics: [{
                    {
                    metric_time: integer,
                    trial: integer,
                    episode_status: string,
                    reward_score, integer
                    completion_percentage: integer,
                    elapsed_time_in_milliseconds: integer,
                    start_time: integer,
                    episode: integer,
                    phase: string
                    },
                    {
                    repeat
                    }
                    repeat ...
                    ]
    sim-trace
        training
            <14 digit date time>-<22 character URL>
                training-simtrace
                    0-iteration.csv (rows = episodes * steps)
                        episode
                        steps
                        X
                        Y
                        yaw
                        steer
                        throttle
                        action
                        reward
                        done
                        all_wheels_on_track
                        progress
                        closest_waypoint
                        track_len
                        tstamp
                        episode_status
                    1-iteration.csv
                        repeat
                    2-iteration.csv
                    repeat ...
                    7-iteration.csv

3. EVALUATION data

[your model name]

    logs
        evaluation
            "evaluation-<14 digit date time>-<22 character URL>-robomaker.log
    metrics
        evaluation
            evaluation-<14 digit date time>-<22 character URL>.json
                {metrics: [{
                    {
                    completion_percentage: integer,
                    immobilized_count: integer,
                    off_track_count: integer,
                    elapsed_time_in_milliseconds: integer,
                    episode_status: string,
                    metric_time: integer,
                    reset_count: integer,
                    reversed_count: integer,
                    crash_count: integer,
                    start_time: integer,
                    trial: integer,
                    },
                    {
                    repeat
                    }
                    repeat ...
                    ]
    sim-trace
        evaluation
            <14 digit date time>-<22 character URL>
                training-simtrace
                    0-iteration.csv
                        episode
                        steps
                        X
                        Y
                        yaw
                        steer
                        throttle
                        action
                        reward
                        done
                        all_wheels_on_track
                        progress
                        closest_waypoint
                        track_len
                        tstamp
                        episode_status
                    1-iteration.csv
                        repeat
                    2-iteration.csv
                    repeat ...
                    7-iteration.csv

4. LEADERBOARD data

[your model name]

    logs
        leaderboard
            "evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>-robomaker.log

** the 22 character URL is base64 encoding without padding as suggested by this link:
https://security.stackexchange.com/questions/194092/what-encryption-algorithm-outputs-22-characters-string

