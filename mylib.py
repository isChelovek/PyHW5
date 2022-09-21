def init():
  '''Чистит экран и делает оступ'''  
  from os import system
  system("cls")
  print()

def Get_Int_Num():
    '''Безопасный целочисленный ввод с консоли'''
    while type:
        input_string = input('Введите число - ')
        try:
            number_float = int(input_string)
            return number_float
        except ValueError:
            print('Это не число') 

def GetIntWithLowLimit(minValue):
    check = True
    while check:
        userNum = Get_Int_Num()
        if userNum < minValue:
            print(f'Число должно быть больше {minValue-1}')
        else:
            break
    return userNum

def GetIntWithLowAndHightLimit(minValue, maxValue):
    check = True
    while check:
        userNum = Get_Int_Num()
        if minValue <= userNum <= maxValue: #Такие вещи нравятся в питоне
            break
        else:
            print(f'Число должно находится в диапазоне {minValue} <= "Ваше число" <= {maxValue}')
            
    return userNum