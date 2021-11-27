#!/usr/bin/env python3
import sys

def calendar(date):
    print(date)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'calendar':
            calendar(sys.argv[2])
        else:
            print(sys.argv[1])
    else:
        print("Usage: dctl.py action args")

