# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

import re
import mylib
mylib.init()

def deleting_pattern1(delete_here):
    '''Способ 1 через регулярные выражения'''
    x = re.findall(r'\b[^абв].*', delete_here) # Сложно составлять. Можно ли в регулярное выражение добавить переменную?
    return ''.join(x)
   
def deleting_pattern2(pattern, delete_here):
    '''Способ 2 через генерацию, наверное'''
    result = ['' if pattern in i  else i for i in re.split(r'\b', delete_here)] # re.split(r'\b', delete_here) очень удобно
    return ''.join(result)

def deleting_pattern3(pattern, delete_here):
    '''Способ 3 похож на второй'''
    return ''.join(x for x in re.split(r'\b', delete_here) if x.find(pattern))

def deleting_pattern(delete_here):
    '''Способ 1 через регулярные выражения'''
    x = re.findall(r'\w', delete_here) # Сложно составлять. Можно ли в регулярное выражение добавить переменную?
    print(x)

print('Программа удаляет все слова содержащие "абв" из строки "абвгдейка - это передача"')
print(deleting_pattern1('абвгдейка - это передача'))
print(deleting_pattern2('абв', 'абвгдейка - это передача'))
print(deleting_pattern3('абв', 'абвгдейка - это передача'))