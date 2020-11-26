"""Submit to Dynamo"""

import os
from decimal import Decimal
from statistics import mean

import boto3

TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(TABLE_NAME)

    submission = event['data']

    response = table.put_item(
        Item={
            'track_meta_eval': submission['track_meta_eval'],
            'name': submission['name'],
            'speed_max': Decimal(str(submission['speed_max'])),
            'steer_max': Decimal(str(submission['steer_max'])),
            'avg_completion_pct_eval': Decimal(str(mean(submission['completion_pcts_eval']))),
        }
    )

    print(response)

    return {
        'status_code': 200,
        'response': response
    }
