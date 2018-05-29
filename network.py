#!/usr/bin/python
import os
import requests

SECRET_KEY = 'GLPKP'
baseURL = 'http://upe.42069.fun/' + SECRET_KEY
def get_data():
    r = requests.get(baseURL)
    data = r.json()
#    print(data)
    state = data.get('state', "")
    status = data.get('status', "")
    remaining_guesses = data.get('remaining_guesses', "")
    return data #state, status, remaining_guesses

def post_data(guess):
    payload = {'guess': guess}
    r = requests.post(baseURL, data=payload)
    data = r.json()
 #   print(data)
    state = data.get('state', "")
    status = data.get('status', "")
    remaining_guesses = data.get('remaining_guesses', "")
    win_rate = data.get('win_rate', "")
    games = data.get('games', "")
    lyrics = data.get('lyrics', "")
    return data #, state, status, remaining_guesses, win_rate, games, lyrics

def reset_data(email):
    payload = {'email': email}
    r = requests.post(baseURL + '/reset', data=payload)
    data = r.json()
#    print(data)
    return data.get('success')


if __name__ == "__main__":
    print(get_data())
    print(post_data)
    print(reset_data)
