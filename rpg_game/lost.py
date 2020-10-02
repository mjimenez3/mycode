rooms = {
    # Lost Island
    'Survivor\'s Beach': {
        'west': 'Sun\'s Garden',
        'north': 'Caves',
        'east': 'Cockpit',
        'desc': 'This is the site where your plane has crashed and you all set up camp.'
    },
    'Sun\'s Garden': {
        'east': 'Survivor\'s Beach',
        'west': 'Mr. Eko\'s Church',
        'desc': 'Sun\'s Garden...she\'s not here, take something to eat.',
        'item': 'fruit'
    },
    'Mr. Eko\'s Church': {
        'east': 'Sun\'s Garden',
        'west': 'Four Toed Statue',
        'desc': 'This is also the place where Locke made his sweat box, do you see any visions?'
    },
    'Cockpit': {
        'west': 'Survivor\'s Beach',
        'south': 'Fuselage',
        'north': 'Caves',
        'desc': 'Charlie left his stash, maybe you can get some good vibes if you find it.',
        'item': 'heroin',
    },
    'Caves': {
        'south': 'Survivor\'s Beach',
        'east': 'Cockpit',
        'northeast': 'Heart of the Island',
        'north': 'The Pearl',
        'west': 'The Tempest',
        'desc': 'Camp site #2 for those ready to live on the island, there are bones, and fresh water.',
    },
    # Secret only accessible if you are the protector of the island
    'Heart of the Island': {
        'southwest': 'Caves'
    },
    'Four Toed Statue': {
        'north': 'French Expedition Camp',
        'south': 'Mr. Eko\'s Church',
        'desc': 'All that is left of the statue are the feet. Do you know what lies in the shadow of the statue?'
    },
    'Fuselage': {
        'north': 'Cockpit',
        'east': 'Well',

    },
    'Well': {
        'west': 'Fuselage',
        'south': 'Jacob\'s Cave'
    },
    'Jacob\'s Cave': {
        'north': 'Well',
        'desc': 'On the cave wall you see names, most are crossed out, do you see your name?',

    },
    'Rousseau\'s Camp': {
        'west': 'Well',
        'south': 'Lighthouse',
        'east': 'The Looking Glass'
    },
    'Lighthouse': {
        'north': 'Rousseau\'s Camp',
        'east': 'The Looking Glass',
        'desc': 'You see your name, you move the mirror to your name and see your house, Jacob\'s been watching you.'
    },
    'The Looking Glass': {
        'west': 'Rousseau\'s Camp',
        'south': 'Lighthouse',
        'north': 'Locke\'s Beach'
    },
    'Locke\'s Beach': {
        'south': 'The Looking Glass',
        'west': 'Black Rock',
        'north': 'Hydra Island',
        'desc': 'Beach where you can use a boat to get to Hydra Island.',
        'item': 'Boat',
    },
    'Hydra Island': {
        'south': 'Locke\'s Beach',
        # maybe more
    },
    'Black Rock': {
        'east': 'Locke\'s Beach',
        'south': 'The Pearl',
        'north': 'The Orchid',
        'item': 'Dynamite',
        'desc': 'An old ship from the 1800\'s, in the middle of the island?'
    },
    'The Pearl': {
        'east': 'Black Rock',
        'south': 'Caves',
        'west': 'The Tempest'
    },
    'The Tempest': {
        'east': 'The Pearl',
        'south': 'Caves',
        'north': 'Radio Tower'
    },
    'Radio Tower': {
        'south': 'The Tempest',
        'east': 'The Staff'
    },
    'The Staff': {
        'south': 'Radio Tower',
        'east': 'The Orchid'
    },
    'The Orchid': {
        'west': 'The Staff',
        'south': 'Black Rock',
        'north': 'Barracks'
    },
    'French Expedition Camp': {
        'east': 'Four Toed Statue',
        'west': 'The Door',
    },
    'The Door': {
        'south': 'French Expedition Camp',
        'north': 'The Temple'
    },
    'The Temple': {
        'west': 'The Door',
        'east': 'Barracks'
    },
    'Barracks': {
        'north': 'Boathouse',
        'west': 'The Temple',
        'south': 'The Orchid',
        'east': 'The Flame'
    },
    'Boathouse': {
        'south': 'Barracks'
    },
    'The Flame': {
        'west': 'Barracks',
        'east': 'The Arrow',
        'north': 'Dharma Grave Site',
    },
    'Dharma Grave Site': {
        'south': 'The Flame'
    },
    'The Arrow': {
        'north': 'The Flame',
        'east': 'Tail Section'
    },
    'Tail Section': {
        'west': 'The Arrow',
        'desc': 'The campsite for the people in the tail section of Flight 815.'
    }
}

