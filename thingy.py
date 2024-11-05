clothes_rack = ['dress', 'trousers', 'socks', 'skirt', 'shirt']
print(clothes_rack)

print(clothes_rack[1:3])
print(clothes_rack[1:4])

clothes_rack.extend(['t-shirt', 'shoes', 'cap'])
print(clothes_rack)

clothes_rack.insert(4, 'gloves')
print(clothes_rack)

clothes_rack.remove('shoes')
print(clothes_rack)

del clothes_rack[5]
print(clothes_rack)

last_item = clothes_rack.pop()
print(last_item)

if 'dress' in clothes_rack:
    print('I have found my dress')
else:
    print('I cant find my dress')

print(clothes_rack.index('gloves'))

clothes_rack.sort()
print(clothes_rack)

clothes_rack.reverse()
print(clothes_rack)

for x in clothes_rack:
    print(x)