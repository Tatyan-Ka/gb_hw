# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот
# день выходным.
a = int(input('Введите номер дня недели:'))
bud = [1, 2, 3, 4, 5]
vyh = [6, 7]
if a in bud:
    print('нет')
elif a in vyh:
    print('да')
else:
    print('это не номер дня недели!')
# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = [True, False]
y = x
z = y
for i in range(len(x)):
    for j in range(len(y)):
        for l in range(len(z)):
            print('x=', x[i], 'y=', y[j], 'z=', z[l])
            if not (x[i] or y[j] or z[l]) == (not (x[i]) and not (y[j]) and not (z[l])):
                print('утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно')
            else:
                print('утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно')

# 4. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = float(input('Введите координату x:'))
y = float(input('Введите координату y:'))
if x > 0:
    if y > 0:
        print(1)
    elif y < 0:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    elif y < 0:
        print(3)

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой
# четверти (x и y).
ch = int(input('Введите номер четверти (1-4):'))
if ch == 1:
    print('координаты x>0 y>0')
elif ch == 2:
    print('координаты x<0 y>0')
elif ch == 3:
    print('координаты x<0 y<0')
elif ch == 2:
    print('координаты x>0 y<0')
else:
    print('неверный номер')
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D
# пространстве.
a = [float(i) for i in input('Введите координаты точки (x y) А через пробел: ').split()]
b = [float(i) for i in input('Введите координаты точки (x y) В через пробел: ').split()]
r = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
print("расстояние между точками А и В: ", round(r, 0))

