#!/usr/bin/env python3
#this library allows us to generate UUID values.
import uuid
from  time import sleep
howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs..."); sleep(0.8)

# range is required because an int cannot be looped
for rando in range(howmany):
    print( uuid.uuid4() )

