#wrong importing modules

import sys, os, time, datetime


#correct importing modules

import sys
import os
import time
import datetime

datetime(dir)
#####################################################################
#wrong operator place and indentation
num_1 = 4
num_2 = 7
num_3 = 2
num_4 = 8

print(num_1 +
num_2 +
num_3 +
num_4)

def my_function(
        num_1,
        num_2,
        num_3,
        num_4):
    print(num_1)

#correct operator place and indentation
num_1 = 4
num_2 = 7
num_3 = 2
num_4 = 8

print(
    num_1
    + num_2
    + num_3
    + num_4)


def my_function(
        num_1,
        num_2,
        num_3,
        num_4):
    print(num_1)

###############################
# wrong length of codes (it should be 79 characters long, or 72 if we use docstrings)
long_code_length = ["Please Write a number before: ", "This is another string", "This line length is too much"]
print(len('long_code_length = ["Please Write a number before: ", "This is another string", "This line length is too much"]'))


#correct length of codes
long_code_length = [
    "Please Write a number before: ", 
    "This is another string", 
    "This line length is not too much"
    ]
