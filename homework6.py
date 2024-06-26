my_dict = {'Name': 'Dmitry', 'Age': 20, 'Height': 191}

print(my_dict)
print(f'Имя: {my_dict.get('Name')}\nВес: {my_dict.get('Weight', 'Такого параметра нет')}')

my_dict.update({'Weight': 82,
               'Eye color': 'Brown'})
del_ = my_dict.pop('Age')

print(f'Удаленный параметр: {del_}')
print(my_dict)

#########################################

my_set = {1, 2, 2, 2, 3, 3, 4, 7, 7, 8}

print(f'\n{my_set}')
my_set.update({9, 10, 9})
my_set.discard(1)
print(my_set)