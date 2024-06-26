immutable_var = (12, False, 'Lesson')

print(f'Immutable tuple: {immutable_var}')

mutable_list = [[0, 0], [0, 1], [1, 0], [1, 1]]
mutable_list[0][1] = 1
mutable_list[1][1] = 0

print(f'Mutable list: {mutable_list}')
