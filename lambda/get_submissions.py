"""Retrieve records from DynamoDB"""

import os
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = os.environ['TABLE_NAME']

def lambda_handler(event, context):
    
    dynamo = boto3.resource('dynamodb')
    table = dynamo.Table(TABLE_NAME)

    track_name = event['data']['Track']

    response = table.query(
        KeyConditionExpression=Key('Track').eq(track_name)
    )

    print(response)

    submissions = response['Items']

    return {
        'status_code': 200,
        'submissions': submissions
    }
