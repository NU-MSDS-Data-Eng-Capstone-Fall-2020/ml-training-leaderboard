todo:

  - [x] insert assembler.sh into Makefile
  - [ ] lint, test
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


item

speed_granularity
speed_max
steer_granularity
steer_max
lidar
camera

hyperparameters:
- batch_size
- beta_entropy
- discount_factor
- e_greedy_value
- epsilon_steps
- exploration_type
- loss_type
- lr
- num_episodes_between_training
- num_epochs
- stack_size
- term_cond_avg_score
- term_cond_max_episodes

training_params:
- car_name_train
track_train
episodes_train
model_name_eval
racer_name_eval
track_eval
trials_train
episode_statuses_train
completion_pcts_train
reward_scores_train
elapsed_times_train
metric_times_train
trials_eval
episode_statuses_eval
completion_pcts_eval
reset_counts_eval
crash_counts_eval
off_track_counts_eval
elapsed_times_eval
metric_times_eval
