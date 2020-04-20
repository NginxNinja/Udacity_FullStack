'''
URL: https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/450352d6-5e7e-47e7-aa41-eae3dc4f3cea/concepts/c24c53a6-4388-451d-aa1a-9a254a8b09bc

Chapter 4. Identity and Access Management
Lesson 3: Passwords
Part 11: Practice - Rainbow Tables
'''

# Load the NIST list of 10,000 most commonly used passwords
with open('nist_10000.txt', newline='') as bad_passwords:
    nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:11])

# The following data is a normalized simplified user table
# Imagine this information was stolen or leaked
leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    }, 
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    }, 
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    }, 
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}

# import the hashlib
import hashlib 
# example hash
word = 'blueberry'
hashlib.md5(word.encode()).hexdigest()

# RAINBOW TABLE SOLUTION
import hashlib
rainbow_table = {}

for word in nist_bad:
    hashed_word = hashlib.md5(word.encode()).hexdigest()
    rainbow_table[hashed_word] = word

# Use the Rainbow table to determine the plain text password
for user in leaked_users_table.keys():
    try:
        print(user + ": \t" + rainbow_table[leaked_users_table[user]['md5']])
    except KeyError:
        print(user + ":\t" + '******* hash not found in rainbow table')