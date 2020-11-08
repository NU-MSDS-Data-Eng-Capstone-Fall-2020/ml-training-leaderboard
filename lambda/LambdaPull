from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_data(RacerID, track, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    #assuming we call our dynamodb table "RacerData"
    table = dynamodb.Table('RacerData') 
                                         

    try:
        response = table.get_item(Key={'Racer': racer, 'track': track})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    Racer = get_data("test", oval,)
    if Racer:
        print("Get data succeeded:")
        pprint(movie, sort_dicts=False)
