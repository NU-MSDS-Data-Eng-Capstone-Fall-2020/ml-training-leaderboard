# ml-training-leaderboard
CL Tool for Submitting Models and Tracking Performance Leaderboards




CLT
- [x] reads in complete training json files
  - complete_model / model_name /model_metadata.json
  - complete_model / model_name / ip / hyper_parameters.json
  - complete_model / model_name / training_parametersXXXXX.json
  - complete_model / model_name / eval_parametersXXXXX.json
  - complete_model / model_name / metrics / training / trainingXXXX.json
- [x] writes out to model_data.json file
- [x] writes model_data.json file to DynamoDB record
- [x] retrieves user specified DynamoDB records
