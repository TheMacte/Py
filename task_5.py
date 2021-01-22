"""
 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят,
 и сколько между ними находится букв.
"""

char1 = ord(input('Введите 1-ую букву '))
char2 = ord(input('Введите 2-ую букву '))
if char1 > char2:
    delta = char1 - char2 - 1
elif char1 < char2:
    delta = char2 - char1 - 1
else:
    delta = 0
print(f'Позиция {chr(char1)} = {char1 - 96} \n'
      f'Позиция {chr(char2)} = {char2 - 96} \n'
      f'Между ними {delta}')
