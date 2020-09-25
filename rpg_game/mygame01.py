#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

# I was making a map of the grounds.  I will include a drawing of the map as well of how far I got..

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Bedroom',
        'north': 'Master Bedroom',
        'item': 'key'
    },
    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
        'south': 'Living Room'
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
        'east': 'Den'
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    },
    'Bedroom': {
        'east': 'Hall',
        'west': 'Bathroom'
    },
    'Bathroom': {
        'east': 'Bedroom'
    },
    'Master Bedroom': {
        'south': 'Hall',
        'west': 'Master Bathroom'
    },
    'Master Bathroom': {
        'east': 'Master Bedroom'
    },
    'Den': {
        'west': 'Dining Room',
        'north': 'Backyard',
    },
    'Backyard': {
        'north': 'Forest',
        'west': 'Forest',
        'east': 'Grass Field',
        'south': 'Den'
    },
    'Forest': {
        'north': 'Forest',
        'west': 'Forest',
        'east': 'Woodlands',
        'south': 'Backyard',
        'item': 'Safe Key'
    },
    'Woodlands': {
        'north': 'Woodland',
        'south': 'Grass Field',
        'east': 'Woodlands',
        'west': 'Forest'
    },
    'Grass Field': {
        'north': 'Woodlands',
        'east': 'Forest',
        'west': 'Backyard',
        'down': 'Underground Room'
    },
    'Living Room': {
        'north': 'Kitchen',
        'south': 'Front Porch',
    },
    'Front Porch': {
        'north': 'Living Room',
        'south': 'Front Yard',
        'east': 'Driveway'
    },
    'Front Yard': {
        'north': 'Front Porch',
        'east': 'Driveway',
    },
    'Driveway': {
        'west': 'Front Yard',
        'east': 'Grass Field'
    },
    'Underground Room': {
        'up': 'Grass Field',
        'east': 'Armory',
        'south': 'Round Room',
        'item': 'Torch',
    },
    'Armory': {
        'west': 'Open Room',
        'item': 'Gun',
        'item': 'Rifle',
        'item': 'Knife',
        'north': 'Safe',
    },
    'Safe': {
        'south': 'Armory',
        'item': 'Gun Ammo',
        'item': 'Rifle Ammo',
    },
    'Round Room': {
        'west': 'Dungeon',
        'south': 'Underground Cliffs'
    },
    'Dungeon': {
        'east': 'Round Room',
        'down': 'Secret Room',
    },
    'Secret Room': {
        'up': 'Dungeon',
        'item': 'Key',
        'item': 'Safe Key',
        'item': 'Gun',
        'item': 'Gun Ammo',
        'item': 'Potion',
    },
    'Underground Cliffs': {
        'jump': 'Underground River',

    }
}

# start the player in the Hall
currentRoom = 'Hall'

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

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    ## If a player enters a room with a monster BUT HAS A COOKIE
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
        print('The monster takes your cookie and runs away! Whew!')
        del rooms[currentRoom]['item']
        inventory.remove('cookie')

    ## If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break









