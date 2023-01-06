

import click
import sys
from arcgis.gis import GIS

#from t_users import commands as group1
#from group2 import commands as group2
#from group3 import commands as group3
#from group4 import commands as group4
#from group5 import commands as group5
#from group6 import commands as group6

@click.group()
def entry_point():
    """YEET"""
@entry_point.command()
@click.option("--url",
              prompt="Enter your url URL ")
@click.option("--username",
              prompt="Enter your username ",
              help="This should be your username for your AGOL or Portal.")
@click.option("--password",
              prompt="Enter your password ",
              help="This should be your password for your AGOL or Portal.")

def startUp(url, username, password):
    try:
        gis = GIS(url, username, password)
        click.echo(f"Welcome {gis.users.me}!")
    except Exception as X:
        click.echo(X)

if __name__ == "__main__":
    try:
    #entry_point.add_command(group1.total_count, name='Total Count')
    #entry_point.add_command(group2.version)
    #entry_point.add_command(group3.account_checker, name='Account Checker')
        entry_point()
    except Exception as X:
        click.echo(X)
        sys.exit(1)

    # except Exception as X:
    #    click.echo(X)
    #    sys.exit(1)