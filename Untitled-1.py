a = input('Введите значение переменной "a": ')
b = input('Введите значение переменной "b": ')
result = 0

try:
    result = int(a) / float(b)
except ZeroDivisionError:
    print('Нельзя делить на 0')
except ValueError:
    print('Ошибка типов - все операнды формулы должны быть числом. Присутствует операнд с типом не число.')
except:
    print('Какая-то неизвестная ошибка')
   

print('результат = ' + str(result))