#!/usr/bin/python3
from lost import rooms
from time import sleep

#from playsound import playsound

with open('LostArt.txt', 'r') as pic:
    link = pic.read()
    print(link)


#playsound("Lost intro.mp3")
# Replace RPG starter project with this code when new instructions are live

# I was making a map of the grounds.  I will include a drawing of the map as well of how far I got.

def showInstructions():
    # print a main menu and the commands
    print('''
Lost RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
  eat [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are at ' + currentRoom)
    # print the current inventory
    if "desc" in rooms[currentRoom]:
        print(rooms[currentRoom]['desc'])
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# this is where rooms goes
rooms = rooms

# start the player in the Hall
currentRoom = 'Survivor\'s Beach'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    if move[0] == 'eat':
        if "item" in inventory == 'fruit':
            print("Eating good fruit, makes musical toots!")
        else:
            print("you have no food available.")

    # Define how a player can win
    # if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    # print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    # break

    # If a player enters a room with a monster BUT HAS A COOKIE
    # if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    # print('The monster takes your cookie and runs away! Whew!')
    # del rooms[currentRoom]['item']
    # inventory.remove('cookie')

    # If a player enters a room with a monster
    # elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    # print('A monster has got you... GAME OVER!')
    # break

