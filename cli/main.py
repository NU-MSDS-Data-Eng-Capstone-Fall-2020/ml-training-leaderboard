"""Entrypoint to CLI tool"""

import click


@click.command(name="submit")
@click.option('--track-name', required=True, type=str)
@click.option('--name', required=True, type=str)
@click.option('--save-local', required=False, type=str)
def submit(track_name, name, save_local=False):
    """Submits new entry to leaderboard"""
    pass


@click.command(name="get-submissions")
@click.option('--track-name', required=True, type=str)
def submit(track_name, name, save_local=False):
    """Gets all entries in leaderboard for specified track"""
    pass
