'''
loads the headlined json files from the tar files: model_meta_data, hyper_parameters.json, etc
and loads relevant data into python (default) dictionary
which is then loaded into 'model_data.json' json file for upload to DynamoDB items space.
'''

# complete_model / model_name / model_metadata.json

    model_data = json.load model_data_template
    model_meta_data = json.load model_metadata
    model_action_space = model_metadata(‘action_space’)
    for i in [‘steering_angle’, ‘speed’]:
        make_values_list from model_action_space[i]
        make_set = set(list)
        count = len(make_set)
        interval = max - min / (n-1)
        model_data[i+’count’] = count
        model_data[i+’interval’] = interval

    model_sensors = model_metadata(‘sensor’)
    for i in model_sensors:
        if i == ’STEREO_CAMERAS’:
            model_data[‘stereo’] = 1
            model_data[‘mono’] = 0
        elif i == ‘MONO_CAMERA’:
            model_data[‘mono’] = 1
            model_data[‘stereo’] = 1
        if i ==‘SECTOR_LIDAR’:
            model_data[‘lidar’] = 1
        else:
            model_data[‘lidar’] =0

    model_data[‘neural_net’] = model_meta_data[‘neural_network’]
    model_data[‘layers’] = model_meta_data[‘version’] #<— unsure about this one

# complete_model / model_name / ip / hyper_parameters.json

    hyperparameters_get = [‘batch_size’, ‘discount_factor’, ‘e_greedy_value’, ‘epsilon_steps’, ‘lr’, ‘num_episodes_between_training’, ‘num_epochs’, ‘stack_size’, ‘term_cond_max_episodes’]
    hyperparameters = json.load hyperparameters.json

    for i in hyperparameters_get:
        model[i] = hyperparameters[i]

# complete_model / model_name / training_parametersXXXXX.json

    training_parameters = json.load training_params_XXXXXXX
    model_data[‘racer_name’] = training_parameters[‘RACER_NAME’]
    model_data[‘car_name’] = training_parameters[‘CAR_NAME’]
    model_data[‘model_name’] = training_parameters[‘MODEL_NAME’]
    model_data[‘track_train’] = training_parameters[‘WORLD_NAME’] <— assert valid track
    model_data[‘episodes’] = training_parameters[‘NUMBER_OF_EPISODES’]

# complete_model / model_name / eval_parametersXXXXX.json

    model_data[‘track_eval’] = training_parameters[‘WORLD_NAME’] <— assert valid track

# complete_model / model_name / metrics / training / trainingXXXX.json

    '''
    file has metrics for n number of episodes and each episode contains

    {"metrics": [
        {
            "reward_score": 364,
            "episode_status": "Off track",
            "start_time": 28278,
            "metric_time": 35747,
            "elapsed_time_in_milliseconds": 7469,
            "completion_percentage": 9,
            "trial": 1,
            "phase": "training",
            "episode": 1},
            ... on to ...
        {
            "reward_score": 444,
            ...,
            "episode": 2}, ...

    so can assemble these data
    -    list of all trial values
    -    list of all episode values
    -    list of all episode_status values
    -    list of all reward_score values
    -    list of all elapsed_time_in_milliseconds values
    -    list of all completion_percentage values
    -    compute total elapsed time training
    -    compute average percent completion = number of episodes where not Off track / number episodes
    -    compute 3 highest reward laps completed
    -    compute 3 fastest completed laps = ordered list of laps not Off track
    '''
    
# complete_model / model_name / metrics / evaluation / trainingXXXX.json

    '''
    file has metrics for n number of trials and each trail contains:

    {"metrics": [
        {
            "trial": 1,
            "start_time": 8809,
            "episode_status": "Crashed",
            "reversed_count": 0,
            "completion_percentage": 3,
            "immobilized_count": 0,
            "reset_count": 1,
            "crash_count": 1,
            "elapsed_time_in_milliseconds": 4173,
            "off_track_count": 0,
            "metric_time": 12982},
            ... on to ...
        {
            "trail": 2,
            ...}, ...

        so can assemble these data
        -    list of all trial values
        -    list of all episode_status values
        -    list of all completion_percentage values
        -    list of all reset_count values
        -    list of all crash_count values
        -    list of all off_track_count values
        -    list of all elapsed_time_in_milliseconds values
        -    compute average percent completion = number of episodes where not Off track / number episodes
        -    compute 3 fastest completed laps = ordered list of laps not Off track

    '''
