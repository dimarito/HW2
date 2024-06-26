my_dict = {'Name': 'Dmitry', 'Age': 20, 'Height': 191}

print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Name')}\nNot existing value: {my_dict.get('Weight', 'Такого параметра нет')}')

my_dict.update({'Weight': 82,
               'Eye color': 'Brown'})
del_ = my_dict.pop('Age')

print(f'Deleted value: {del_}')
print(f'Modified dictionary: {my_dict}')

#########################################

my_set = {1, 2, 2, 2, 3, 3, 4, 7, 7, 8}

print(f'\nSet: {my_set}')
my_set.update({9, 10, 9})
my_set.discard(1)
print(f'Modified set: {my_set}')