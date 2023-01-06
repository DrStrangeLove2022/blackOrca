import click

@click.group(name='version')
def version():
    """Display Current Version"""
    click.echo("0.0.1")
#def _read_version():
        #return "0.0.1"

@version.command(name='test', help='test')
@click.option('--test', default='1', help='test option')
def test(test1):
    click.echo("Hello Test")

@version.command(name='testing', help='testing')
@click.option('--testing', default='1', help='testing option')
def test(test1):
    click.echo("Hello Testing")

if __name__ == '__main__':
    version()

