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

Usage:

```shell
Push 1: 
python slack.py --stoken "token url" --channel "channel" --push post --random no
 --message "message"

Push 2: 
python slack.py --stoken "token url" --channel "channel" --push post --random yes
 --gtoken "token_url" --search "funny cats"

Pull 1: python slack.py --stoken "token url" --channel "channel" --push get
```

Example: Image is Copyrighted (giphy)

![Imgur Image](http://i.imgur.com/kaxpwSz.png)

