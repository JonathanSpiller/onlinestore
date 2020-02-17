import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'instock': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'instock': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'instock': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'instock': True
        },
    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data




