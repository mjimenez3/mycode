#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    # display the methods available to our new object
    print(r.json() )

    # Create 3 new lines via the escape character \n
    print("\n\n\n")

    # if we request the 'all' key, we can strip off the outside {}
    # This seems minor, but is CRITICAL if we want to parse our data
    print(r.json().get("all"))


main()

