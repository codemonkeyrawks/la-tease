# Date: 4/22/2019
# Author: codemonkeyrawks
# Licence: CC-BY-SA 4.0
# Description: Slack Bot Message Parser

# Library: CMD Parsing, REST Stack
import argparse
import requests

# --------------------- Parser Section ------------------------------ #

# Options: API + Title + Message
parser = argparse.ArgumentParser(description='Slack Bot Message Parser')
parser.add_argument('--stoken', help='Slack Token KEY', type=str)
parser.add_argument('--gtoken', help='Giphy Token KEY', type=str)
parser.add_argument('--channel', help='Channel Posted In', type=str)
parser.add_argument('--message', help='Body of Message', type=str)
parser.add_argument('--push', help='POST or GET', type=str)
parser.add_argument('--random', help='Random Image', type=str)
parser.add_argument('--search', help='Search Image', type=str)

# Print Help on -H or -h
args = parser.parse_args()

# --------------------- Slack API Section --------------------------- #

# Process: Outbound Messages
def p0Send(stoken, channel, message):
    try:
        stat0 = requests.post('https://slack.com/api/chat.postMessage', headers= { 'Authorization': 'Bearer {}'.format(stoken) }, json={'text': message, 'channel': "#" + channel })
        stat1 = stat0.json()
        print(("Status : %s") % (stat1["ok"]))
    except:
        print("Error: Message was not sent")

# Process: Inbound Messages
def p0Rec(stoken, channel):
    try:
        stat0 = requests.get('https://slack.com/api/channels.history', headers= { 'Authorization': 'Bearer {}'.format(stoken) })
        stat1 = stat0.json()
        print(("Status : %s") % (stat1["ok"]))
    except:
        print("Error: Message was not collected")

# Process: Random Message : Images
def p1Send(stoken, channel, message, ptoken, search):
    try:
        stat0 = requests.get("http://api.giphy.com/v1/gifs/search?" + "q=" + search + "&api_key=" + ptoken + "&limit=1")
        stat1 = stat0.json()
        stat2 = stat1["data"][0]["images"]["downsized"]["url"]
        print(stat2)
        stat3 = requests.post('https://slack.com/api/chat.postMessage', headers= { 'Authorization': 'Bearer {}'.format(stoken) }, json={'text': stat2, 'channel': "#" + channel })
        stat4 = stat3.json()
        print(("Status : %s") % (stat4["ok"]))
    except:
        print("Error: Message was not sent")

# --------------------- Process Control Section --------------------- #

# Options: API + Title + Message
if (args.stoken == None):
    print('')
    print("Error: Please Specify a Correct Slack Token Key")
    print('')
elif (args.channel == None):
    print('')
    print("Error: Please Specify a Channel")
    print('')
elif (args.push == None):
    print('')
    print("Error: Please Specify Push Flag")
    print('')
elif (args.random == None):
    print('')
    print("Error: Please Specify Random Flag")
    print('')
else:
    # GET, POST OR ERROR on Slack
    if (args.push.lower() == "get"):
          p0Rec(args.stoken, args.channel)
    elif (args.push.lower() == "post"):
        if (args.message == None):
            print('')
            print("Error: Please Specify Message")
            print('')
        else:
            if (args.random.lower() == "no"):
                p0Send(args.stoken, args.channel, args.message)
            else:
                if (args.gtoken == None):
                    print('')
                    print("Error: Please Specify a Correct Giphy Token Key")
                    print('')
                else:
                    if (args.search == None):
                        print('')
                        print("Error: Please Specify a Correct Search String")
                        print('')
                    else:
                        p1Send(args.stoken, args.channel, args.message, args.gtoken, args.search)
    else:
        print("Error: Please Specify GET or POST")
