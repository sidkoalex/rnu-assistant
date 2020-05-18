db.jobs.insert([
    {
        'name': 'SAY_THIS',
        'search_type': 'STARTS_WITH_MATCH',
        'search_data': ['скажи', 'повтори']
    },
    {
        'name': 'HELLO',
        'search_type': 'EXACT_MATCH',
        'search_data': 'привет'
    },
        {
        'name': 'HELLO',
        'search_type': 'EXACT_MATCH',
        'search_data': 'hello'
    },
    {
        'name': 'TURN_OFF_SCREEN',
        'search_type': 'EXACT_MATCH',
        'search_data': 'выключить экран'
    }
])