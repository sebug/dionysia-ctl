#!/usr/bin/env python3
import sys
import os
import requests
from uuid import uuid4

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

def login(email, password):
    device_identifier = str(uuid4())
    request_url = ApiUrl + '/login'
    payload = {}
    payload['email'] = email
    payload['password'] = password
    payload['deviceId'] = device_identifier
    r = requests.post(request_url, json=payload)
    response_json = r.json()
    print(response_json['token'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'calendar':
            calendar(sys.argv[2])
        elif sys.argv[1] == 'login':
            login(sys.argv[2], sys.argv[3])
        else:
            print(sys.argv[1])
    else:
        print("Usage: dctl.py action args")

