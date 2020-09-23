#!/usr/bin/env python3

#for every dirty dish on the table


def counter():
    table= ["plate", "cup", "bowl", "spoon"]

    for dish in table:
        print(f"You left your {dish} on the table! Imma slap you!")

#counter()


def throwaway():
#for every toy in hallway, throw away

    hallway= ["on", "off", "on", "off"]
    spanking= 0
    for toy in hallway:
        print(f"If I see a light on in the hallway, you get a spanking.")
        if toy == "on":
            spanking +=1
            print(f"That's {spanking} spanking you get!")
             
        

#throwaway()


def giving():
    reportcard= ['a', 'b', 'a','c','d']
    wallet = 0
    print("Let's look at your grades, for every A, you get $3, B, $2, and C, $1.")
    for grade in reportcard:
        print(f"You got {grade}")
        if grade == 'a':
            wallet +=3
        elif grade == 'b':
            wallet +=2
        elif grade == 'c':
            wallet +=1
    print(f"You now have ${wallet}!")    

#giving()



#loop challenge
def farmchallenge():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
#easy
    for farm in farms:
        if farm['name'] == "NE Farm":
            for animals in farm["agriculture"]:
                print(animals)
#medium
    user = input("Pick a farm( NE, SE, W)"):
    for farm in farms:
        if farm['name'] == user:
            for agriculture in farm["agriculture"]:
                print(agriculture)

#hard
#    have user input to select a farm and only print the animals from that farm




