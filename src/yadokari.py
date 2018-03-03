import click

RESERVATION_INFO = '''
*** YOUR INFORMATION ***
0. check in date: {check_in_date}
1. check out date: {check_out_date}
2. your name: {name}
3. email address: {email}
4. how many people: {num_of_pople}
************************
'''


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


VALUE_TO_PROMPT = [
    ('check_in_date', lambda: click.prompt('check in date')),
    ('check_out_date', lambda: click.prompt('check out date')),
    ('name', lambda: click.prompt('your name')),
    ('email', lambda: click.prompt('email address')),
    ('num_of_pople', lambda: click.prompt('how many people')),
]


@cmd.command()
@click.argument('context', nargs=-1)
def reserve(context):
    """宿の予約を行う """
    info = {}
    for i, m in VALUE_TO_PROMPT:
        info[i] = m()

    click.echo(RESERVATION_INFO.format(**info))
    confirm = click.prompt('confirm(Y/y) or edit(0-{}): '.format(len(VALUE_TO_PROMPT)))
    while confirm not in ('Y', 'y', 'YES', 'Yes', 'yes'):
        try:
            confirm = int(confirm)
            i, m = VALUE_TO_PROMPT[confirm]
            info[i] = m()
        except:
            pass
        click.echo(RESERVATION_INFO.format(**info))
        confirm = click.prompt('confirm(Y/y) or edit(0-{}): '.format(len(VALUE_TO_PROMPT)))
    click.echo('done!!')


def main():
    cmd()


if __name__ == '__main__':
    main()
