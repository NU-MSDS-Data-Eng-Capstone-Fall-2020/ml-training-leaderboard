todo:

  - [x] insert assembler.sh into Makefile
  - [ ] lint, test
  - [ ] checks: train = eval track e.g.
  - [ ] checks: ensure employing COPY of user's data
  - [ ] code to enable user to identify their tar file
  - [ ] filter hyperparameters to smaller set
  - [ ] checks: train = eval track e.g.
  - [ ] checks: ensure employing COPY of user's data
  - [ ] code to enable user to identify their tar file
  - [ ] filter hyperparameters to smaller set
  - [x] ordered dict
  
outline:

  model_data_assembly.py
  - [x] copy users tar data, unzip
  - [x] load hyperparameters.json directly wholely; can be more selective.
  - [x] load training_params.yaml and from there selected items.
  - [x] call training_data module
  - [x] call evaluation_data module


###source file, item, data type (integer if not noted)

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


## 3 new file trees downloadable from AWS DR

### 3 identically named top folders <your model name> in quotes with data components inside:

<your model name>

    logs
        leaderboard
            "evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>-robomaker.log

<your model name>

    logs
        evaluation
            "evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>-robomaker.log
    metrics
        evaluation
            evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>.json
                completion_percentage
                immobilized_count
                off_track_count
                elapsed_time_in_milliseconds
                episode_status
                metric_time
                reset_count
                reversed_count
                crash_count
                start_time
                trial
    sim-trace
        evaluation
            <14 digit date time>-<22 character URL-base64 encoding without padding**>
                evaluation-simtrace
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
    
<your model name>

    logs
        evaluation
            "evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>-robomaker.log
    metrics
        evaluation
            evaluation-<14 digit date time>-<22 character URL-base64 encoding without padding**>.json
                {metrics: [{
                    {
                    completion_percentage: integer,
                    immobilized_count: integer,
                    off_track_count: integer,
                    elapsed_time_in_milliseconds: integer,
                    episode_status: integer,
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
                    ]
    sim-trace
        training
            <14 digit date time>-<22 character URL-base64 encoding without padding**>
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
                    2-iteration.csv
                    ...
                    7-iteration.csv





** https://security.stackexchange.com/questions/194092/what-encryption-algorithm-outputs-22-characters-string

