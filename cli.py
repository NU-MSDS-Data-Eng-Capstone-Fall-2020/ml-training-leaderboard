"""Entrypoint to CLI tool"""

import json

import boto3
import click
from prettytable import PrettyTable

from assembler.model_data_assembly import make_dict, retrieve_path

SUBMIT_LAMBDA = 'LeaderBoardLambdaStack-submit-handler'
GET_LAMBDA = 'LeaderBoardLambdaStack-get-handler'


@click.group()
def cli():
    pass


@cli.command(name="submit")
@click.option('--track-name', required=True, type=str)
@click.option('--name', required=True, type=str)
@click.option('--save-local', required=False, type=str)
def submit(track_name, name, save_local=False):
    """Submits new entry to leaderboard"""

    paths = retrieve_path()
    data = make_dict(*paths)
    data['name'] = name

    client = boto3.client('lambda', region_name='us-east-1')
    response = client.invoke(
        FunctionName=SUBMIT_LAMBDA,
        Payload=json.dumps({
            'data': data
        })
    )

    print("Successfully submitted model")


@cli.command(name="get-submissions")
@click.option('--track-name', required=True, type=str)
def get_submissions(track_name):
    """Gets all entries in leaderboard for specified track"""
    
    client = boto3.client('lambda', region_name='us-east-1')
    response = client.invoke(
        FunctionName=GET_LAMBDA,
        Payload=json.dumps({
            'data': {'track_meta_eval': track_name}
        })
    )

    leaders = json.loads(response['Payload'].read())['submissions']
    leaders = sorted(leaders, key=lambda k: k['avg_completion_pct_eval'], reverse=True) 

    table = PrettyTable()
    table.field_names = leaders[0].keys()
    table.add_rows(
        _.values() for _ in leaders
    )
    print(table.get_string())


if __name__ == '__main__':
    cli()

