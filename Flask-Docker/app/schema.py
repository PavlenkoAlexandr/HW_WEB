

AD_CREATE = {
    'type': 'object',
    'properties': {
        'name': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
        'created_date': {
            'type': 'string',
            'pattern': """(\d{4})-(\d{2})-(\d{2})"""
        },
        'owner': {
            'type': 'string'
        },
    },
    'required': ['name', 'description', 'created_date', 'owner', ],
}
