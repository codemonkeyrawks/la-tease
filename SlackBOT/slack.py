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
parser.add_argument('--push', help='POST or GET', type=str)

# Print Help on -H or -h
args = parser.parse_args()

# Process: Outbound Messages
def postInput(token, channel, message):
    try:
        stat0 = requests.post('https://slack.com/api/chat.postMessage', headers= { 'Authorization': 'Bearer {}'.format(token) }, json={'text': message, 'channel': "#" + channel })
        stat1 = stat0.json()
        print(("Status : %s") % (stat1["ok"]))
    except:
        print("Error: Message was not sent")

# Process: Inbound Messages
def pushInput(token, channel):
    try:
        stat0 = requests.get('https://slack.com/api/channels.history', headers= { 'Authorization': 'Bearer {}'.format(token) })
        stat1 = stat0.json()
        print(("Status : %s") % (stat1["ok"]))
    except:
        print("Error: Message was not collected")

# Options: API + Title + Message
if (args.token == None):
    print('')
    print("Error: Please Specify a Correct Token Key")
    print('')
elif (args.channel == None):
    print('')
    print("Error: Please Specify a Channel")
    print('')
elif (args.message == None):
    print('')
    print("Error: Please Specify a Body Message")
    print('')
else:
    # GET OR POST
    if (args.push == "GET" or args.push == "get"):
        pushInput(args.token,args.channel)
    else:
        postInput(args.token,args.channel,args.message)
