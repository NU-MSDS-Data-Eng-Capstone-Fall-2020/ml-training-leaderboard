"""Submit to Dynamo"""

import os
from decimal import Decimal

import boto3

TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(TABLE_NAME)

    submission = event['data']

    response = table.put_item(
        Item={
            'Track': submission['Track'],
            'Metric': submission['Metric'],
            'Person': submission['Person'],
            'Accuracy': Decimal(str(submission['Accuracy']))
        }
    )

    print(response)

    return {
        'status_code': 200,
        'response': response
    }
