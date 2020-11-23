# assembler

## todo:

  - [ ] document in code, lint, test, CICD
  - [ ] ensure hyperparameters are the same in training, evaluation, leaderboard log files.
  - [ ] ensure: train log time ~ eval log time ~ leaderboard log time 



## getting it running:

1.  Create your model.  Train your model.  Evaluate your model.  Compete your model in virtual qualifier to obtain a leaderboard ranking.
    -   Model name
    -   Environment simulation 
    -   Race type --> ```Time Trial```
    -   Agent: Choose a vehicle from garagae --> ```Edit``` button
        -   Camera or Stereo camera
        -   LIIDAR Sensor
    -   Action space
        -   Maximum steerring angle
        -   Steering angle granularity
        -   Maximum speed
        -   Speed granularity
    -   Name your DeepRacer
        -   ```Done``` button
    -   Reward function
    -   Hyperparameters
    -   Stopping conditions
<img width="1197" alt="Pasted Graphic 39" src="https://user-images.githubusercontent.com/38410965/99921188-c4c8c100-2cf6-11eb-9d92-4706e1b2fc23.png">

... after creating, training, evaluating, competing for ranking ...

2.  ```Actions``` --> ```Download physical car model``` menu item:
<img width="1197" alt="modeldepp" src="https://user-images.githubusercontent.com/38410965/99921207-dad68180-2cf6-11eb-8e6f-19746510f325.png">

3.  ```Download logs``` button for Training and Evaluation: 
<img width="1197" alt="modeldepp" src="https://user-images.githubusercontent.com/38410965/99921257-2f79fc80-2cf7-11eb-990b-943c445406d8.png">

4.  ```Download logs``` button for leaderboard.  
<img width="1311" alt="2020 October Qualifier" src="https://user-images.githubusercontent.com/38410965/99921314-9eefec00-2cf7-11eb-81ad-8291e34c63a8.png">

5.  Downloads will appear as the model folder and three duplicate folders:
<img width="537" alt="Items, 980 08 GB available" src="https://user-images.githubusercontent.com/38410965/99922334-10cb3400-2cfe-11eb-87ab-703ee62b1dae.png">

6.  Make a directory, get inside, clone the repo, get inside the assembler folder, and call the python code:
<img width="682" alt="renote Enumerating objects 107, done" src="https://user-images.githubusercontent.com/38410965/99922337-14f75180-2cfe-11eb-9ec0-96d927317860.png">

7.  Follow the instructions at the top of the finder window to find the ```model_metadata.json``` file:
<img width="912" alt="Pasted Graphic 1" src="https://user-images.githubusercontent.com/38410965/99922342-19236f00-2cfe-11eb-9691-605f6e73aed8.png">

8.  Follow the instructions at the top of the finder window to find the ```training-*-*-robomaker.log``` file:
<img width="1299" alt="Pasted Graphic 2" src="https://user-images.githubusercontent.com/38410965/99922349-217baa00-2cfe-11eb-8591-3cce17a8d102.png">

9.  Follow the instructions at the top of the finder window to find the ```evaluation-*-*-robomaker.log``` file:
<img width="1310" alt="Pasted Graphic 3" src="https://user-images.githubusercontent.com/38410965/99922354-2a6c7b80-2cfe-11eb-8815-d0ae3c41735e.png">

10. Follow the instructions at the top of the finder window to find the ```leaderboard-*-*-robomaker.log``` file:
<img width="1310" alt="Pasted Graphic 4" src="https://user-images.githubusercontent.com/38410965/99922360-322c2000-2cfe-11eb-9a1b-c8ee6838dfb0.png">

11. Drink a sip of wine. You're done.  Here is your ```model_data.json``` file:
<img width="1283" alt="Pasted Graphic 6" src="https://user-images.githubusercontent.com/38410965/99922369-3a845b00-2cfe-11eb-905b-c5721002e894.png">



## outline of the seven modules:

###  ```model_data_assembly.py```
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
  
  ### ```metadata_model.py```
  
  When you set up your model, you specify a race car's steering and speed with 4 parameters.  AWS DeepRacer combines all possible pairs of these 4 speed and steering parameters to produce a much larger set of parameters.  That larger set of parameters is saved into ```model_metadata.json``` that you've downloaded.  This module converts that larger set of parameters back to the original 4 parameters, and adds in sensor settings as binaries.
  
  ###  ```hyperparameters.py``` and ```metadata_stage.py```
  
  Both modules use similar methods to parse the log files for the hyperparameters and meta data from the training, evaluation and leaderboard stages.  Presently, only use hyperparameters from training stage.  A check should be put in place to ensure all 3 hyperparameters are the same.
  
  ### ```results_evaluation.py``` and ```results_training.py```
  
  Both assemble a dictionary of lists from the ```*metrics.json``` files in the ```training``` and ```leaderboard``` folders.

  ###  ```path.py```
  
  Uses ```tkinter``` package, which is the standard Python interface to the ```Tk``` GUI toolkit, to let the user open a finder window with a title guiding the user to find and select the needed file in their file system.  This module ensures the user only selects required file type (```*.log``` or ```*.json``` depending on the situation), ensures that the user selects a ```robomaker.log``` and not ```sagemaker.log``` file, ensures the user only selects ```training``` or ```evaluation``` or ```leaderboard``` file when requested.  If user fails in this regard, the finder window pops up again to let the user try again.  The function returns a path to the desired file.  For training, evaluation and leaderboard files, a ```*.log``` file is found by the user and the module uses this path to find a ```.json``` file and that path is returned as well.  Here's the specifics:

#### model data:
- via tkinter finder window guides user to point to file path as follows:

    ```[your model name]-model/model_metadata.json```

- code confirms that the file path:
    - [x] includes ```model```
    - [x] ends in ```*.json```
- returns via:

    ```path_metadata_model = path.finder('model’)```

#### training data:
- via tkinter finder window guides user to point to file path as follows:

    ```[your model name]/logs/training/training-<14 digit date time>-<22 character URL>-robomaker.log```
    
- code confirms that the file path:
    - [x] includes ```training```
    - [x] ends in ```*.log```
    - [x] does not include ```sagemaker```
    
- automatically finds metrics (aka results) path at:

    ```[your model name]/metrics/training/training-<14 digit date time>-<22 character URL>.json```
    
- returns via:

    ```path_logs_training, path_training_results = path.finder('training’)```

#### evaluation data:
- via tkinter finder window guides user to point to file path as follows:

    ```[your model name]/logs/evaluation/evaluation-<14 digit date time>-<22 character URL>-robomaker.log```
- code confirms that the file path:
    - [x] includes ```evaluation``` 
    - [x] ends in ```*.log```
- automatically finds metrics (aka results) path at:

    ```[your model name]/metrics/evaluation/evaluation-<14 digit date time>-<22 character URL>.json```
- returns via:

    ```path_logs_evaluation, path_evaluation_results = path.finder('evaluation’)```

#### leaderboard data:
- via tkinter finder window guides user to point to file path as follows:

    ```[your model name]/logs/leaderboard/leaderboard-<14 digit date time>-<22 character URL>-robomaker.log```
- code confirms that the file path:
    - [x] includes ```leaderboard```
    - [x] ends in ```*.log```
- returns via: 

    ```path_logs_leaderboard = path.finder('leaderboard’)```



## source files, items & data types (```i``` integer, ```f``` float, ```s``` string, and list):

**metadata from model** from the ```[your model name]-model/model_metadata.json``` file:
- speed_granularity ```i```
- speed_max ```i```
- steer_granularity ```i```
- steer_max ```i```
- lidar ```i binary```
- camera ```i binary``` 

**hyperparameters** from the ```[your model name]/logs/training/training-*-*-robomaker.log``` file:
- batch_size ```i```
- beta_entropy ```f```
- discount_factor ```f```
- e_greedy_value ```f```
- epsilon_steps ```i```
- exploration_type ```s```
- loss_type ```s```
- lr ```f```
- num_episodes_between_training ```i```
- num_epochs ```i```
- sac_alpha ```f```
- stack_size ```i```
- term_cond_avg_score ```f```
- term_cond_max_episodes ```i```

**metadata from training stage** from the ```[your model name]/logs/training/training-*-*-robomaker.log``` file:
- track_meta_train ```s```

**metadata from evaluation stage** from the ```[your model name]/logs/evaluation/evaluation-*-*-robomaker.log``` file:
- model_name_meta_eval ```s```
- racer_name_meta_eval ```s```
- track_meta_eval ```s```
- trials_meta_eval ```i```

**metadata from leaderboard stage** from the ```[your model name]/logs/leaderboard/leaderboard-<14 digit date time>-<22 character URL>-robomaker.log``` file:
- trials_meta_lead ```s```
- track_meta_lead ```s```

**results from training** from the ```[your model name]/metrics/training/training-*-*.json``` file are in the form of a dict of list of ```i```, ```f```, or ```s``` from all training epsisodes:
- trials_train ```list of i```
- episodes_train ```list of i```
- episode_statuses_train ```list of s```
- completion_pcts_train ```list of i```
- reward_scores_train ```list of i```
- elapsed_times_train ```list of i```
- metric_times_train ```list of i```

**results from evaluation** from the ```[your model name]/metrics/evaluation/evaluation-*-*.json``` file are in the form of a dict of list of ```i```, ```f```, or ```s``` from all evaluation epsisodes:
- trials_eval ```list of i```
- episode_statuses_eval ```list of s```
- reset_counts_eval ```list of i```
- crash_counts_eval ```list of i```
- off_track_counts_eval ```list of i```
- completion_pcts_eval ```list of i```
- elapsed_times_eval ```list of i```
- metric_times_eval ```list of i```



## four folders are downloadable from AWS DR: here are their file trees:

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
                training-<14 digit date time>-<22 character URL>-sagemaker.log
                training-<14 digit date time>-<22 character URL>-robomaker.log
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
                evaluation-<14 digit date time>-<22 character URL>-robomaker.log
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
                        1-iteration.csv
                            repeat
                        2-iteration.csv
                        repeat ...
                        7-iteration.csv

4. LEADERBOARD data

    [your model name]
    
        logs
            leaderboard
                evaluation-<14 digit date time>-<22 character URL>-robomaker.log

** the 22 character URL is base64 encoding without padding as suggested by this link:
https://security.stackexchange.com/questions/194092/what-encryption-algorithm-outputs-22-characters-string

