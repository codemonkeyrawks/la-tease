# Date: 4/22/2019
# Author: codemonkeyrawks
# Licence: CC-BY-SA 4.0
# Description: Slack Bot Message Parser

# Library: CMD Parsing, REST Stack
import argparse
import requests

# Options: API + Title + Message
parser = argparse.ArgumentParser(description='Slack Bot Message Parser')
parser.add_argument('--token', help='Slack Token KEY', type=str)
parser.add_argument('--channel', help='Channel Posted In', type=str)
parser.add_argument('--message', help='Body of Message', type=str)

# Print Help on -H or -h
args = parser.parse_args()

# Options: API + Title + Message
if (args.token == None):
    print('')
    print("Please Specify a Correct Token Key")
    print('')
elif (args.channel == None):
    print('')
    print("Please Specify a Channel")
    print('')
elif (args.message == None):
    print('')
    print("Please Specify a Body Message")
    print('')
else:
    temp = "#" + args.channel
    posting = requests.post('https://slack.com/api/chat.postMessage', headers= { 'Authorization': 'Bearer {}'.format(args.token) }, json={'text': args.message, 'channel': temp })
