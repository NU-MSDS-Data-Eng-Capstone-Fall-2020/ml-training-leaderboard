"""Entrypoint to CLI tool"""

import boto3
import click
# import prettytable  need to use this for printing


@click.command(name="submit")
@click.option('--track-name', required=True, type=str)
@click.option('--name', required=True, type=str)
@click.option('--save-local', required=False, type=str)
def submit(track_name, name, save_local=False):
    """Submits new entry to leaderboard"""

    # TODO: add assembly code here

    #data = assembler.run(fn1, fn2, ..)

    # TODO: invoke submit Lambda function here

    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='',
        Payload={
            'data': 'INSERT_ASSEMBLED_DATA'
        }
    )

    pass


@click.command(name="get-submissions")
@click.option('--track-name', required=True, type=str)
def submit(track_name, name, save_local=False):
    """Gets all entries in leaderboard for specified track"""
    
    # TODO: invoke get_submissions Lambda function here
    client = boto3.client('lambda')
    response = client.invoke(
        FunctionName='',
        Payload={
            'data': {'Track': track_name}
        }
    )

    # TODO: print leaderboard
