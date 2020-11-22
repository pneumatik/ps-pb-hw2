password = input('Введите пароль: ')

numeric = password.isnumeric()
blank = len(password)
pss = 1
#result = 'Привет'


# try:
#     pss = float(pss)   
# except ValueError:
#     print('OK')

try: # проверяем только числа
    numeric = 1 / (1 - numeric)
    #print(result)
    
except ZeroDivisionError:
    print('Ваш пароль состоит только из цифр')
    

try: # проверяем пустой пароль
    blank = 1 / blank
except ZeroDivisionError:
     print('Вы ввели пустой пароль')

try: # все в порядке
    pss = bool(password)

except ValueError:
    print('OK')




# print('OK')
# print(password)ghgkhjkh
# print('pss ' + str(pss))
#
#print('цифра ' + str(numeric))
# print('пусто ' + str(blank))




