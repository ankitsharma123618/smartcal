#!/usr/bin/env python3
import sys
sys.path.append('')
import math
from math import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("enter your queries\n")
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()] (l[0],l[1])
                print(r)
            except:
                print("something went wrong, please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()] ()
            break
    else:
        sorry()


