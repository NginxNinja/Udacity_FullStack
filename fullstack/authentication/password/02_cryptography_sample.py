'''
URL: https://classroom.udacity.com/nanodegrees/nd0044/parts/b91edf5c-5a4d-499a-ba69-a598afd9fe3e/modules/5606de9d-aa2b-4a1b-9b14-81b87d80a264/lessons/450352d6-5e7e-47e7-aa41-eae3dc4f3cea/concepts/5adc5ff8-1728-4163-9271-9db65ba1089c

Chapter 4. Identity and Access Management
Lesson 3: Passwords
Part 8: Practice - Using Cryptography
'''

# Import package
from cryptography.fernet import Fernet

# Generate a Key and Instatiate Fernet instance
key = Fernet.generate_key()
f = Fernet(key)
print(key, ", key")

# Define our message
plaintext = b"encryption is very useful"

# Encrypt
ciphertext = f.encrypt(plaintext)
print(ciphertext)

# Decrypt
decryptedtext = f.decrypt(ciphertext)
print(decryptedtext)

## Exercise
key_exercise = b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
f_exercise = Fernet(key_exercise)
print(key_exercise,', key_exercise')

message = b'gAAAAABc8Wf3rxaime-363wbhCaIe1FoZUdnFeIXX_Nh9qKSDkpBFPqK8L2HbkM8NCQAxY8yOWbjxzMC4b5uCaeEpqDYCRNIhnqTK8jfzFYfPdozf7NPvGzNBwuuvIxK5NZYJbxQwfK72BNrZCKpfp6frL8m8pdgYbLNFcy6jCJBXATR3gHBb0Y='
decrypt_exer01 = f_exercise.decrypt(message)
print(decrypt_exer01)

message2 = b'encrypting is just as useful'
encrypt_exer02 = f_exercise.encrypt(message2)
print(encrypt_exer02, ', encrypt_exer02')