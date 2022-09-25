# -*- coding: utf-8 -*-
def prov_chislo(a: str):
    cnt = 0
    res = True
    for i in range(len(a)):
        if i == 0 and (a[i] == '-' or a[i].isdigit()):
            res = True
        elif not a[i].isdigit() and a[i] != '.':
            res = False
        elif a[i] in '.':
            cnt += 1
        if cnt > 1:
            res = False
    return res


def prov_deist(y):
    operations = ['+', '-', '*', '/']
    if y in operations:
        return True
    else:
        return False


x = input('Введите число:')
d = input('Введите действие:')
print(prov_chislo(x))
print(prov_deist(d))
