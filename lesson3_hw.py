# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной
# позиции.
#  Пример:
#  - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
spisok = [int(i) for i in input('Введите значения элементов через пробел: ').split()]
s = 0
for i in range(len(spisok)):
    if i % 2 == 1:
        s += spisok[i]
print('сумма нечетных элементов =', s)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: # - [2, 3, 4, 5, 6] => [12, 15, 16]; - [2, 3, 5, 6] => [12, 15]

spis2 = [int(i) for i in input('Введите значения элементов через пробел: ').split()]
proizv = []
dl_sp = round(len(spis2) / 2) + len(spis2) % 2
for i in range(dl_sp):
    proizv.append(spis2[i] * spis2[(len(spis2)-1 - i)])
print(spis2, '=>', proizv)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

fl_list = []
dm_list = []
for element in input('введи вещественные числа через пробел: ').split():
    fl_list.append(float(element))
    if 0 != round(float(element) % 1, 10):
        dm_list.append(round(float(element) % 1, 10))
x = max(dm_list) - min(dm_list)
print(fl_list, '=>', x)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# # Пример:#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = int(input('Введите число:'))
res = ''
i = x
while i // 2 != 0:
    res += str(i % 2)
    i = i // 2
x_dv = '1' + ''.join(reversed(res))
print(x, '=>', x_dv)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
#  - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
mem = {1: 1, 2: 1, -1: 1, -2: -1}


def fib(n):
    if n not in mem:
        mem[n] = fib(n - 1) + fib(n - 2)
    return mem[n]


def fib_nega(n):
    if n not in mem:
        mem[n] = fib(n + 2) - fib(n + 1)  # F(n+2)−F(n+1)
    return mem[n]


fib_lst = []
fib_lst_n = []
for i in range(int(input('Введите число:'))):
    fib_lst.append(fib(i))
    fib_lst_n.append(fib_nega(-i))
fib_lst_n.reverse()
res = fib_lst_n[:(i - 1)] + fib_lst
print(res)

