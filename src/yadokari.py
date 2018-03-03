import click


@click.group()
def cmd():
    pass


@cmd.command(name='list')
def show_list():
    """宿の一覧を表示 """
    click.echo('omishima-space')


@cmd.command()
@click.argument('context', nargs=-1)
def show(context):
    """宿の詳細URLを表示 """
    if context:
        click.echo('https://omishima-space.com/')


@cmd.command()
@click.argument('context', nargs=-1)
@click.option('--month', '-m', default=1)
@click.option('--year', '-y', default=2018)
def cal(context, year, month):
    """宿の予約状況を表示 """
    import calendar
    print(calendar.month(year, month))


@cmd.command()
@click.argument('context', nargs=-1)
@click.option('--check_in_date', prompt='check in date',
               help='check in date')
@click.option('--check_out_date', prompt='check out date',
               help='check out date')
@click.option('--name', prompt='your name',
               help='your name')
@click.option('--email', prompt='email address',
               help='email address')
@click.option('--num_of_people', prompt='how many people',
               help='how many people')
def reserve(context, check_in_date, check_out_date, name, email, num_of_people):
    """宿の予約を行う """
    click.echo(check_out_date)
    click.echo(check_in_date)
    click.echo(name)
    click.echo(email)
    click.echo(num_of_people)

def main():
    cmd()


if __name__ == '__main__':
    main()

