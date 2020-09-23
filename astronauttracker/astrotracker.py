#!/usr/bin/env python3

import requests

def main():
    # request for astronaut tracker, use .json() method to make persistant to not have to call it again
    # .json() will translate from json to python readable.
    r= requests.get('http://api.open-notify.org/astros.json').json()
    

    # for loop taking r number, and iterating that many times for people
    print(f"People in space: {r['number']}")
    for astros in r['people']:
        print(f"{astros['name']} on the {astros['craft']}")


    #hard coding how the people. 
    print(f"People in space: {r['number']}")
    print(f"{r['people'][0]['name']} on the {r['people'][0]['craft']}")
    print(f"{r['people'][1]['name']} on the {r['people'][1]['craft']}")
    print(f"{r['people'][2]['name']} on the {r['people'][2]['craft']}")
    







main()
