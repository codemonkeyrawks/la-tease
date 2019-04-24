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
1. Push Message: python slack.py --token "token url" --channel "channel" --message "message" --push POST/post
2. Pull Message: python slack.py --token "token url" --channel "channel" --push GET/get
```
