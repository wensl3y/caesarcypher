# FORK

import string

s = input('Введите текст: ')
s = s.upper()

letters_lat = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # len = 26
letters_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' # len = 33
result = ''

while s:
    print('Чтобы засекретить сообщение, вбивайте число БОЛЬШЕ нуля.\nЧтобы рассекретить сообщение, вбейте число МЕНЬШЕ нуля.\nМожно ввести значение только от -25 до 25')
    try:
        k = int(input('Введите число: '))
    except ValueError:
        print('Повторите ввод.')
    else:
        if (k==0) or (k>25) or (k<-25):
            print('Повторите ввод.')
        else:
            break

for symbol in s:
    
    if symbol in letters_lat:  # Ищет символ в латинице
        num = letters_lat.find(symbol)
        num += k
        
        if num >= len(letters_lat):
            num -= len(letters_lat)    
        elif num < 0:
            num += len(letters_lat)
            
        result += letters_lat[num]
    
    elif symbol in letters_rus:   # Ищет символ в кириллице 
        num = letters_rus.find(symbol)
        num += k
        
        if num >= len(letters_rus):
            num -= len(letters_rus) 
        elif num < 0:
            num += len(letters_rus)
            
        result += letters_rus[num]
    
    else:
        result += symbol
    
print('Результат: {}'.format(result))
