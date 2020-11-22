password = input('Введите пароль: ')

numeric = password.isnumeric()
blank = len(password)

try: # проверяем только числа
    numeric = 1 / (1 - numeric)    
except ZeroDivisionError:
    print('Ваш пароль состоит только из цифр')
try: 
    blank = 1 / blank + int(password)
except ZeroDivisionError: # проверяем пустой пароль
     print('Вы ввели пустой пароль')
except ValueError: # проверяем отсутсвие проблем
    print('Требования к паролю соблюдены')
