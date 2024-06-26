my_string = input('Введите произвольный текст: ')

print(f'Количество символов текста: {len(my_string)}\nВерхний регистр {my_string.upper()}\nНижний регистр: {my_string.lower()}\nБез пробелов: {my_string.replace(' ', '')}\nПервый символ: {my_string[0]}\nПоследний символ: {my_string[-1]}')
