#Password generator

import string
import secrets

length = int(input('\nEnter the length of the password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

total = lower + upper + numbers + symbols

password = ''.join(secrets.choice(total) for _ in range(length))

print(password)