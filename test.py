# 79
plus1 = int(input('Введите первое положительное число: '))  # Прошу пользователя ввести первое число
plus2 = int(input('Введите второе положительное число: '))    # Прошу пользователя ввести второе число
if plus1>plus2 :          # Нахожу наименьшее из меньших введённых чисел и присваиваю меньшее переменной d
    d = plus2
else:
    d = plus1
while plus1 % d !=0 and plus2 % d !=0:   # Ставлю цикл работы, пока мои два числа делятся без остатка на их наименьшее число
    d = d-1
print('Наибольший общий делитель = ', d) # Выведу перемнную d