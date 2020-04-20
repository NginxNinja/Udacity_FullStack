'''
URL: https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/450352d6-5e7e-47e7-aa41-eae3dc4f3cea/concepts/5b9c6032-b6e5-4030-aa20-188fd35caf52

Chapter 4. Identity and Access Management
Lesson 3: Passwords
Part 13: Practice - Salted, Hashed Passwords
'''

# Import the Python Library
import sys
# !{sys.executable} -m pip install bcrypt
import bcrypt

password = b'studyhard'

# Hash a password for the first time, with a certain number of rounds
salt = bcrypt.gensalt(14)
hashed = bcrypt.hashpw(password, salt)
print(salt)
print(hashed)

# Check a plain text string against the salted, hashed digest
bcrypt.checkpw(password, hashed)
print(bcrypt.checkpw(password, hashed))

# Exercise
print("\nExercise results")

hashed_exer = b'$2b$14$EFOxm3q8UWH8ZzK1h.WTZeRcPyr8/X0vRfuL3/e9z7AKIMnocurBG'
password_exec = [b'securepassword', b'udacity', b'learningisfun']

for loop in password_exec:
    result = bcrypt.checkpw(loop, hashed_exer)
    print (loop, ':', result)