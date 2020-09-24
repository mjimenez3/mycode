#!/usr/bin/env python3
"""Messing with Cat Facts"""

# imports always go at the top of your code
import requests
import random
import sys


print("It's about to get the Cat's Meow up in here with some crazy cat facts")
print()
def main():
    """Run time code"""

    
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts').json()

    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    for catfact in r["all"]:
        enter = input("Press any key to get a cat fact, or 'q' to quit")
        print()
        if enter == 'q':
            sys.exit()
        else:
            print(catfact.get("text"))
            print()
            #print(random.choice(rando))


main()

