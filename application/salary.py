DATA = [
    {'id': 1, 'name': 'Alex', 'age': 22, 'job': 'tech support', 'salary': '20000'},
    {'id': 2, 'name': 'Ivan', 'age': 30, 'job': 'director', 'salary': '200000000000'},
    {'id': 3, 'name': 'Gleb', 'age': 26, 'job': 'programmer', 'salary': '21000'},
    {'id': 4, 'name': 'Nikita', 'age': 27, 'job': 'architector', 'salary': '21000'},
]


def calculate_salary(index=None):
    if index:
        result = [
            d['salary']
            for d in DATA
            if d['id'] == index
        ]
    else:
        result = [
            d['salary']
            for d in DATA
        ]
    print(f'Requested salary: {result}')
    return result
