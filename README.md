# Technical Task - Cron Expression Parser 
Cron Expression Parser is a command line application which parses a cron string and expands each field to show the times at which it will run.


## Setting up local development:

Install python 3.11


## Installation

- git clone https://github.com/TimurBatyr/tech_task.git
- cd tech_task
- pip3 install -r requirements.txt

## How to run

- python3 cron_expr_parser.py "*/15 0 1,15 * 1-5 /usr/bin/find"

## Sample output

        Minute        0 15 30 45
        Hour          0
        Day of Month  1 15
        Month         1 2 3 4 5 6 7 8 9 10 11 12
        Day of week   1 2 3 4 5
        Command       /usr/bin/find

