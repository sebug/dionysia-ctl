#!/usr/bin/env python3
import sys
import os

Token=os.environ.get('DIONYSIA_TOKEN')
ApiUrl=os.environ.get('DIONYSIA_API_URL')

def calendar(date):
    print(Token)
    print(ApiUrl)
    print(date)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'calendar':
            calendar(sys.argv[2])
        else:
            print(sys.argv[1])
    else:
        print("Usage: dctl.py action args")

