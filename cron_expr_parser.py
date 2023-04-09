import re
import sys


field_names = ['minute', 'hour', 'day of month', 'month', 'day of week', 'command']

# Minimum and maximum values for each field
min_values = [0, 0, 1, 1, 0, None]
max_values = [59, 23, 31, 12, 6, None]


def check_field(field, i):
    '''Return a list of values that it represents.'''
    if field == '*':
        return list(range(min_values[i], max_values[i] + 1))
    elif '/' in field:
        step = int(field.split('/')[1])
        return list(range(min_values[i], max_values[i] + 1, step))
    elif ',' in field:
        return [int(x) for x in field.split(',')]
    elif '-' in field:
        start = int(field.split('-')[0])
        end = int(field.split('-')[1])
        return list(range(start, end + 1))
    else:
        return [int(field)]

if len(sys.argv) != 2:
    print('Should have only 1 args')
    sys.exit(1)

cron_args = sys.argv[1].split()
if len(cron_args) != 6:
    print('Should have 6 fields')
    sys.exit(1)

for i in range(len(cron_args[:-1])):
    values = check_field(cron_args[i], i)
    print(f"{field_names[i]:14}{' '.join(str(x) for x in values)}")


check_last_field = re.search('[a-zA-Z]+', sys.argv[-1])
'''Check if "/usr/bin/find" in args '''
if check_last_field:
    print(f'{field_names[-1]:14}{cron_args[-1]}')

