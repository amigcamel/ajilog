"""Commandline utilities."""
from io import StringIO
import os.path
import argparse
import configparser
import sys
import json

from . import settings


def _confirm(question, choices=None):
    ans_is_bool = False
    if not choices:
        choices = ('Y', 'n')
        ans_is_bool = True
    ans = None
    while ans not in choices:
        ans = input('{} [{}] '.format(question, '/'.join(choices)))
    if ans_is_bool:
        ans = {'Y': True, 'n': False}[ans]
    return ans


def initialize():
    """Create a config file."""
    if os.path.exists(settings.CONF_NAME):
        ans = _confirm('Conf already exists, do you want to override it')
        if ans is False:
            sys.exit(0)

    config = configparser.ConfigParser()
    use_color = _confirm('Use color?')
    if use_color is True:
        config['stream'] = {
            'color': use_color,
            'level': _confirm(
                'Choose log level:',
                ('debug', 'info', 'warning', 'error', 'critical')
            ),
        }

    use_rotate = _confirm('Enable log rotation?')
    if use_rotate is True:
        config['rotate'] = {
            'enable': use_rotate,
            'level': _confirm(
                'Choose log level:',
                ('debug', 'info', 'warning', 'error', 'critical')),
            'dir': '/tmp/ajilog',
        }

    if not any((use_color, use_rotate)):
        sys.exit(0)
    s = StringIO()
    config.write(s)

    s.seek(0)
    print('\nThis is your configurations:\n\n' + s.read())
    ans = _confirm('\nDo you want to save it?')
    if ans is True:
        with open(settings.CONF_NAME, 'w') as f:
            config.write(f)
        print('Config save successfully!')
    else:
        print('Config will not be saved')
        sys.exit(0)


def gen(save=False):
    """Generate default configurations.

    :param save: write to file if save==True
    """
    s = json.dumps(settings.HANDLERS, indent=4)
    print(s)
    if save:
        with open(settings.CONF_NAME, 'w') as f:
            f.write(s)
        print(settings.CONF_NAME, ' saved!')


def main():
    """Execute argparse."""
    try:
        parser = argparse.ArgumentParser()
        subparser = parser.add_subparsers(dest='command')
        subparser.add_parser('init')
        parser_gen = subparser.add_parser('gen')
        parser_gen.add_argument('--save', action='store_true')

        args = vars(parser.parse_args())
        command = args.pop('command')
        if command == 'init':
            initialize()
        elif command == 'gen':
            gen(**args)
        else:
            parser.print_help()
    except KeyboardInterrupt:
        print('\nAborted by user!')


if __name__ == '__main__':
    main()
