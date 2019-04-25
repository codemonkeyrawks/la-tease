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
1. Push #1: python slack.py --stoken "token url" --channel "channel" --push post --random no --message "message"
2. Push #2: python slack.py --stoken "token url" --channel "channel" --push post --random yes --gtoken "token_url" --search "funny cats"

2. Pull #1: python slack.py --stoken "token url" --channel "channel" --push get
```

Example:

![alt text](https://imgur.com/kaxpwSz "Funny Cat")
