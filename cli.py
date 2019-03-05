"""Commandline utilities."""
from io import StringIO
import os.path
import configparser
import sys


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


conf_name = 'ajilog.conf'


def initialize():
    """Create a config file."""
    if os.path.exists(conf_name):
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
        with open(conf_name, 'w') as f:
            config.write(f)
        print('Config save successfully!')
    else:
        print('Config will not be saved')
        sys.exit(0)


def main():
    """Execute main function."""
    try:
        initialize()
    except KeyboardInterrupt:
        print('\nAborted by user!')


if __name__ == '__main__':
    main()
