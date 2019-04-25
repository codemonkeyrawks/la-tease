Structure:

```shell
Project:
  licence.txt     - CC-BY-SA Licence
  readme.md       - Getting Started Guide

Testing:
  .gitlab-cl.yml  - Build/Test Script: GitLab: TBD
```

Building:

```shell
1. sudo apt-get install git
2. git clone https://github.com/codemonkeyrawks/LATease.git
```

CMD Flags:
```shell
  stoken  = Slack Token
  gtoken  = Giphy Token
  channel = Slack Channel
  message = Slack Message
  push    = POST OR GET
  random  = YES OR NO
  search  = Giphy Search
```

Usage:

This projects main goal is to take in user action input and fork out tweaked messages
baised on the inputted string. Ex: clock would return 10:02 AM UTC. This project also
supports giphy images which can be used for other things like breakage.


```shell
Push 1: 
python slack.py --stoken "token url" --channel "channel" --push post --random no
 --message "message"

Push 2: 
python slack.py --stoken "token url" --channel "channel" --push post --random yes
 --gtoken "token_url" --search "funny cats"

Pull 1: (*todo)
python slack.py --stoken "token url" --channel "channel" --push get
```

Example: Image is Copyrighted (giphy)

![Imgur Image](http://i.imgur.com/kaxpwSz.png)

