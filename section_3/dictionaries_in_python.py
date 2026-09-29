my_dict = {
    'key1': 'value1',
    'key2': 'value2'}

# print(my_dict['key1'])

prices_lookup = {
    'apple': 2.99,
    'oranges': 1.99,
    'milk': 5.80
}
# print(prices_lookup['apple'])

d = {
    'k1': 123,
    'k2': [0, 1, 2],
    'k3': {
        'insideKey': 100
    }
}
# print(d['k2'])
# print(d['k3']['insideKey'])
# print(d['k2'][2])

d = {
    'key1': ['a', 'b', 'c']
}

my_list = d['key1']
letter = my_list[2]
# print(letter.upper())

my_list = d['key1'][2].upper()
# print(my_list)

d = {'k1': 100, 'k2': 200}
d['k3'] = 300
# print(d)

d['k1'] = 'NEW VALUE'

d = {'k1': 100, 'k2': 200, 'k3': 300}

# print(d)
# print(d.keys())
# print(d.values())
print(d.items())
