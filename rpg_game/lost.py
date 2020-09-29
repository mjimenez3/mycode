rooms = {
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
