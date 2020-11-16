#!/bin/bash

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/ip/hyperparameters.json .

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/metrics/evaluation/evaluation*.json evaluation.json 

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/metrics/training/training*.json training.json

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/training_params*.yaml training_params.yaml

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/eval_params*.yaml eval_params.yaml 

cp -r ../downloadable\ AWS\ DR\ console\ files/complete_model/rightangle/model_metadata.json .
