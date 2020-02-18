import json

def create_database(dst_file='my_file.json'):
    data = [
        {
            'id': 0,
            'name': 'iphone 9',
            'price': 799,
            'stock': 3,
            'image': 'iphone9.jpeg'
        },

        {
            'id': 1,
            'name': 'Macbook Pro',
            'price': 4799,
            'stock': 0,
            'image': 'macbookpro.jpeg'
        },

        {
            'id': 2,
            'name': 'Apple Watch',
            'price': 10799,
            'stock': 3,
            'image': 'applewatch.jpeg'
        },

        {
            'id': 3,
            'name': 'Android Phone',
            'price': 99999,
            'stock': 5,
            'image': 'androidphone.jpeg'
        }
    ]

    with open(dst_file, 'w') as f:
        json.dump(data, f, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def update_database(products, src_file='my_file.json'):
    with open(src_file, 'w') as f:
        json.dump(products, f, indent=4)
        print("database updated...")



