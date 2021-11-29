#!/usr/bin/env python3
import sys
import os
import requests

Token=os.environ.get('DIONYSIA_TOKEN')
ApiUrl=os.environ.get('DIONYSIA_API_URL')

def calendar(date):
    request_url = ApiUrl + '/getCalendar/' + date
    headers = { "Authorization": "Bearer " + Token }
    response = requests.get(request_url, headers = headers)
    structured = response.json()
    lessons = structured['lessons']
    print('Your lessons for ' + date)
    for lesson in lessons:
        print(lesson['type'])
        print('From ' + lesson['start'] + ' to ' + lesson['end'])
        print('At ' + lesson['teren']['name'] + ', ' + lesson['teren']['address'])
        for coach in lesson['coaches']:
            print('By ' + coach['name'])
        print('with')
        for student in lesson['students']:
            print(' ' + str(student['status']) + ' ' + student['name'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'calendar':
            calendar(sys.argv[2])
        else:
            print(sys.argv[1])
    else:
        print("Usage: dctl.py action args")

