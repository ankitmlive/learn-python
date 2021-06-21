"""""""""""""""""""""""""""""""""""""
""" Leap Year Check in Python """""""
"""""""""""""""""""""""""""""""""""""

year = 1992
def is_leap(year):
    leap = False
    if year%4 is 0:
        if year%100 is 0:
            if year%400 is 0:
                leap = True
            else:
            	leap = False
        else:
        	leap = True
    else:
        leap = False
    return leap
    
x = is_leap(year)
print(x)

""""""""""""""""""""""""""""""""""""""""""""""
""""    Cube Volume where n is len       """""
"""" Volume = length x width x height    """""
""""""""""""""""""""""""""""""""""""""""""""""

n = 3
def cube(n):
	return n**3
x = cube(n)
print(x)

## Result : 27

"""""""""""""""""""""""""""""""""""""""""""""""
"""" List Comprehensions 
"""" creating a list with prev. cube function
"""""""""""""""""""""""""""""""""""""""""""""""

xList = range(1,11)
x = [cube(x) for x in xList] 
print(x)

# Result : [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

## EXAMPLE - 2

print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
# This code is equvalent to :
results = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        results.append([x, y])

print(results)

Result : [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]] -- for both case

### TOTP Wrapper
# -*- coding: utf-8 -*-
import time

import pyotp
from pyotp import TOTP

# from django_otp.oath import TOTP
# from django_otp.util import random_hex


# ToDo: use django-otp if it doesnt work nw
class TOTPVerification:
    def __init__(self):
        # secret key that will be used to generate a token,
        # User can provide a custom value to the key.
        self.key = pyotp.random_base32()
        # counter with which last token was verified.
        # Next token must be generated at a higher counter value.
        self.last_verified_counter = -1
        # this value will return True, if a token has been successfully
        # verified.
        self.verified = False
        # number of digits in a token. Default is 6
        self.number_of_digits = 6
        # validity period of a token. Default is 30 second.
        self.token_validity_period = 35
        self.interval = 60

    def totp_obj(self):
        # create a TOTP object
        # totp = TOTP(key=self.key,
        #             step=self.token_validity_period,
        #             digits=self.number_of_digits)
        totp = TOTP(self.key, interval=120)
        # the current time will be used to generate a counter
        #totp.time = time.time()
        return totp

    def generate_token(self):
        # get the TOTP object and use that to create token
        totp = self.totp_obj()
        # token can be obtained with `totp.token()`
        token = totp.now()
        return token

    def verify_token(self, token, tolerance=0):
        try:
            # convert the input token to integer
            token = int(token)
        except ValueError:
            # return False, if token could not be converted to an integer
            self.verified = False
        else:
            totp = self.totp_obj()
            # check if the current counter value is higher than the value of
            # last verified counter and check if entered token is correct by
            # calling totp.verify_token()
            # if ((totp.t() > self.last_verified_counter) and
            #         (totp.verify(token, tolerance=tolerance))):
            if totp.verify(token):
                # if the condition is true, set the last verified counter value
                # to current counter value, and return True
                # self.last_verified_counter = totp.t()
                self.verified = True
            else:
                # if the token entered was invalid or if the counter value
                # was less than last verified counter, then return False
                self.verified = False
        return self.verified
