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
        'down': 'Underground River',
    },    'Underground River': {
        'south': 'Castle Landing',
    },
    'Castle Landing': {
        'south': 'Outer Gatehouse',
        'west': 'Dovecote',
    },
    'Dovecote': {
        'east': 'Castle Landing',
    },
    'Outer Gatehouse': {
        'south': 'Courtyard',
        'north': 'Castle Landing',
    },
    'Courtyard': {
        'east': 'Stables',
        'west': 'Chapel',
        'south': 'Gatehouse',
        'north': 'Outer Gatehouse'
    },
    'Stables': {
        'west': 'Courtyard',
    },
    'Chapel': {
        'east': 'Courtyard',
    },
    'Gatehouse': {
        'north': 'Courtyard',
        'south': 'Lower Foyer',
        'east': 'Garrison\'s Quarters'
    },
    'Garrison\'s Quarters': {
        'north': 'Dungeon',
        'south': 'Castle Tunnel',
    },
    'Lower Foyer': {
        'north': 'Gatehouse',
        'west': 'West Gallery',
        'east': 'East Gallery',
        'south': 'Upper Foyer',
    },
    'Upper Foyer': {
        'north': 'Lower Foyer',
        'west': 'Castle Dining Room',
        'east': 'Study',
        'south': 'Great Hall',
    },
    'Great Hall': {
        'north': 'Upper Foyer',
        'south': 'Fountain',
        'west': 'Castle Kitchen',
        'east': 'Sitting Room',
    },
    'Study': {
        'west': 'Upper Foyer',
        'south': 'Sitting Room',
    },
    'Fountain': {
        'north': 'Great Hall'
    },
    'Sitting Room': {
        'north': 'Study',
        'west': 'Great Hall',
        'east': 'East Hallway',
    },
    'East Hallway': {
        'north': 'East Gallery',
        'east': 'Master Suite',
        'west': 'Sitting Room',
    },
    'East Gallery': {
        'east': 'East Deck',
        'south': 'East Hallway',
        'west': 'Lower Foyer',
    },
    'East Deck': {
        'west': 'East Gallery',
    },
    'Water Closet': {
        'south': 'Master Suite'
    },
    'Master Suite': {
        'north': 'Water Closet',
        'south': 'Master Deck',
        'east': 'East Hallway'
    },
    'Master Deck': {
        'north': 'Master Suite'
    },
    'West Gallery': {
        'east': 'Lower Foyer',
        'south': 'West Hallway',
        'west': 'Laundry Room',
    },
    'Laundry Room': {
        'east': 'West Gallery'
    },
    'Castle Dining Room': {
        'east': 'Upper Foyer',
        'south': 'Butler Pantry',
        'west': 'West Hallway'
    },
    'Butler Pantry': {
        'north': 'Castle Dining Room',
        'south': 'Castle Kitchen',
        'down': 'Tunnel',
    },
    'Castle Tunnel': {
        'up': 'Butler Pantry',
        'south': 'Labyrinth',
    },
    'Castle Kitchen': {
        'north': 'Butler Pantry',
        'east': 'Great Hall',
        'south': 'Playroom',
        'west': 'Breakfast Nook',
    },
    'Playroom': {
        'north': 'Castle Kitchen',
        'south': 'Family Deck',
        'west': 'Family Room',
    },
    'Family Deck': {
        'north': 'Playroom',
        'west': 'Family Room',
    },
    'Family Room': {
        'north': 'Breakfast Nook',
        'east': 'Playroom',
        'south': 'Family Deck',
    },
    'Breakfast Nook': {
        'north': 'West Hallway',
        'east': 'Castle Kitchen',
        'south': 'Family Room',
        'west': 'Covered Terrace',
    },
    'Covered Terrance': {
        'east': 'Breakfast Nook'
    },
    'West Hallway': {
        'north': 'West Gallery',
        'east': 'Castle Dining Room',
        'south': 'Breakfast Nook',
        'west': 'Conservatory',
    },
    'Conservatory': {
        'east': 'West Hallway',
    },
    'Labyrinth': {
        'north': 'Castle Tunnel',
        'east': 'MA',
        'south': 'RP',
        'west': 'AM',
    },
    'AM': {
        'east': 'Labyrinth',
        'west': 'NM',
    },
    'NM': {
        'south': 'RI',
        'east': 'AM',
    },
    'RI': {
        'north': 'NM',
        'south': 'PA',
        'east': 'AE',
    },
    'PA': {
        'north': 'RI',
        'south': 'HI',
    },
    'HI': {
        'north': 'PA',
        'south': 'FF',
    },
    'FF': {
        'north': 'HI'
    },
    'AE': {
        'west': 'RI',
        'south': 'AQ'
    },
    'AQ': {
        'north': 'AE',
        'south': 'DZ',
    },
    'DZ': {
        'north': 'AQ',
        'south': 'AC'
    },
    'AC': {
        'north': 'DZ',
        'east': 'BF'
    },
    'ZT': {
        'south': 'AZ',
        'east': 'AO'
    },
    'AZ': {
        'north': 'ZT',
        'east': 'AG',
    },
    'MT': {
        'east': 'BB'
    },
    'LL': {
        'east': 'CA',
    },
    'AO':   {
        'west': 'ZT',
        'east': 'QM',
    },
    'AG': {
        'west': 'AZ',
        'south': 'BB',
        'east': 'GM'
    },
    'BB': {
        'north': 'AG',
        'west': 'MT',
        'east': 'AA',
    },
    'CA': {
        'west': 'LL',
        'east': 'DF'
    },
    'RP': {
        'north': 'Labyrinth',
        'south': 'DQ',
    },
    'DQ': {
        'north': 'RP',
        'east': 'AD'
    },
    'AI': {
        'south': 'BF'
    },
    'BF': {
        'north': 'AI',
        'west': 'AC',
        'south': 'QM'
    },
    'QM': {
        'north': 'BF',
        'west': 'AO'
    },
    'GM': {
        'west': 'AG',
        'east': 'YM',
    },
    'AA': {
        'west': 'BB'
    },
    'DF': {
        'west': 'CA',
        'east': 'Maze'
    },
    'FC': {
        'east': 'TA'
    },
    'AD': {
        'east': 'DQ',
        'west': 'AP',
    },
    'DL': {
        'east': 'BG',
        'south': 'AH',
    },
    'AH': {
        'north': 'DL',
        'east': 'AJ'
    },
    'AB': {
        'south': 'YM'
    },
    'YM': {
        'west': 'GM'
    },
    'BA': {
        'south': 'Maze'
    },
    'RM': {
        'west': 'MA',
        'south': 'TA'
    },
    'TA': {
        'north': 'RM',
        'west': 'FC',
        'east': 'LZ'
    },
    'AP': {
        'west': 'AD',
        'south': 'BG'
    },
    'BG': {
        'north': 'AP',
        'west': 'DL'
    },
    'AJ': {
        'west': 'AH',
        'south': 'DB',
        'east': 'IT'
    },
    'DB': {
        'north': 'AJ',
        'east': 'BH'
    },
    'AK': {
        'south': 'RR'
    },
    'RR': {
        'north': 'AK',
        'south': 'XS',
        'east': 'QE'
    },
    'XS': {
        'north': 'RR',
        'west': 'Maze'
    },
    'SO': {
        'south': 'LZ',
        'east': 'MN',
    },
    'LZ': {
        'west': 'TA',
        'north': 'SO'
    },
    'BI': {
        'south': 'ST'
    },
    'ST': {
        'north': 'BI',
        'south': 'IT',
    },
    'IT': {
        'north': 'ST',
        'west': 'AJ',
        'south': 'BH'
    },
    'BH': {
        'north': 'IT',
        'west': 'DB'
    },
    'UP': {
        'east': 'WO',
        'south': 'QE',
    },
    'QE': {
        'north': 'UP',
        'west': 'RR',
        'south': 'PP'
    },
    'PP': {
        'north': 'QE',
        'east': 'VA'
    },
    'MN': {
        'west': 'SO',
        'south': 'VD'
    },
    'VD': {
        'north': 'MN',
        'south': 'WE'
    },
    'WE': {
        'north': 'VD',
        'south': 'NV'
    },
    'NV': {
        'north': 'WE',
        'south': 'LE'
    },
    'LE': {
        'north': 'NV',
        'south': 'GL'
    },
    'GL': {
        'north': 'LE',
        'south': 'WO'
    },
    'WO': {
        'north': 'GL',
        'west': 'UP',
        'south': 'CD'
    },
    'CD': {
        'north': 'WO',
    },
    'VA': {
        'west': 'PP'
    },
    'MA': {
        'west': 'Labyrinth',
        'east': 'RM'
    },
    'Maze': {
        'east': 'XS',
        'north': 'BA',
        'west': 'DF'
    },
    # Lost Island
    'Survivor\'s Beach': {
        'west': 'Sun\'s Garden',
        'north': 'Caves',
        'east': 'Cockpit',
    },
    'Sun\'s Garden': {
        'east': 'Survivor\'s Beach',
        'west': 'Mr. Eko\'s Church',
    },
    'Mr. Eko\'s Church': {
        'east': 'Sun\'s Garden',
        'west': 'Four Toed Statue'
    },
    'Cockpit': {
        'west': 'Survivor\'s Beach',
        'south': 'Fuselage',
        'north': 'Caves'
    },
    'Caves': {
        'south': 'Survivor\'s Beach',
        'east': 'Cockpit',
        'northeast': 'Heart of the Island',
        'north': 'The Pearl',
        'west': 'The Tempest'
    },
    # Secret only accessible if you are the protector of the island
    'Heart of the Island': {
        'southwest': 'Caves'
    },
    'Four Toed Statue': {
        'north': 'French Expedition Camp',
        'south': 'Mr. Eko\'s Church'
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
        'north': 'Well'
    },
    'Rousseau\'s Camp': {
        'west': 'Well',
        'south': 'Lighthouse',
        'east': 'The Looking Glass'
    },
    'Lighthouse': {
        'north': 'Rousseau\'s Camp',
        'east': 'The Looking Glass'
    },
    'The Looking Glass': {
        'west': 'Rousseau\'s Camp',
        'south': 'Lighthouse',
        'north': 'Locke\'s Beach'
    },
    'Locke\'s Beach': {
        'south': 'The Looking Glass',
        'west': 'Black Rock',
        'north': 'Hydra Island'
    },
    'Hydra Island': {
        'south': 'Locke\'s Beach',
        # maybe more
    },
    'Black Rock': {
        'east': 'Locke\'s Beach',
        'south': 'The Pearl',
        'north': 'The Orchid',
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
        'west': 'The Arrow'
    }
}
