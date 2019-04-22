# Date: 4/22/2019
# Author: codemonkeyrawks
# Licence: CC-BY-SA 4.0
# Description: Slack Bot Message Parser

# Library: CMD Parsing
import argparse

# Options: API + Title + Message
parser = argparse.ArgumentParser(description='Slack Bot Message Parser')
parser.add_argument('--api', help='Slack API KEY', type=str)
parser.add_argument('--title', help='Title of Message', type=str)
parser.add_argument('--message', help='Body of Message', type=str)

# Print Help on -H or -h
args = parser.parse_args()

# Options: API + Title + Message
if (args.api == None):
    print('')
    print("Please Specify a Correct API Key")
    print('')
elif (args.title == None):
    print('')
    print("Please Specify a Title Message")
    print('')
elif (args.message == None):
    print('')
    print("Please Specify a Body Message")
    print('')
else:
    print("OK")
