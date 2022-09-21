# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# -*- coding: utf-8 -*-
# with open('abv.txt', 'w') as f1:
#     f1.write('Напиабвшите программу, удаляюабвщую из текста все слоабвва, содержащие ""абв""')
#
# with open('abv.txt', 'r') as f:
#     s = f.read().splitlines()
# s1 = list(s[0].split())
# print(s1)
# s_new = list(filter(lambda x: 'абв' not in x, s1))
# sw = ''
# for el in s_new:
#     sw += ' ' + el
# print(sw)
#
# with open('abv.txt', 'w') as f:
#     f.write(sw)
#
# # 2. Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета.
# # Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# # За один ход можно забрать не более чем 28 конфет.
# # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# # игроку, чтобы забрать все конфеты у своего конкурента?
# def hod(player_num, count):
#     n = 0
#     while n == 0:
#         if count < 28:
#             n = (input(f'Игрок {player_num}, осталось {count} конфет. Введите кол-во конфет от 1 до {count}:'))
#         else:
#             n = (input(f'Игрок {player_num}, осталось {count} конфет. Введите кол-во конфет от 1 до 28:'))
#         if n.isdigit():
#             if int(n) > 28 or int(n) < 1 or int(n) > count:
#                 print("Ошибка! Введите корректное кол-во конфет")
#                 n = 0
#         else:
#             print("Ошибка! Введите корректное кол-во конфет")
#             n = 0
#     return int(n)
#
#
# import random
#
# cnt: int = 2021  # всего конфет
# p1 = input('Введите имя первого игрока:')
# p2 = input('Введите имя второго игрока:')
# flag = random.randint(0, 1)
# while cnt > 0:
#     if flag:
#         n1 = hod(p1, cnt)
#         cnt -= n1
#         print(f'{p1} взял {n1} конфет. Осталось {cnt}. Ход переходит игроку {p2}')
#         flag = 0
#     else:
#         n2 = hod(p2, cnt)
#         cnt -= n2
#         print(f'{p2} взял {n2} конфет. Осталось {cnt}. Ход переходит игроку {p1}')
#         flag = 1
# if flag:
#     print(f'Игрок {p2} забирает все конфеты')
# else:
#     print(f'Игрок {p1} забирает все конфеты')
#
# # a) Добавьте игру против бота. Достаточно сделать так, чтобы бот не брал конфет больше положенного или больше чем
# # имеется в куче.
#
#
# # b) Подумайте как наделить бота ""интеллектом"". Напоминаю, если перед пользователем будет лежать 29 конфет, то он,
# # однозначно, проиграет. Достаточно довести игру до такой ситуации.
# cnt: int = 2021  # всего конфет
# p1 = input('Введите имя игрока:')
# flag = random.randint(0, 1)
# if flag:
#     print(f'Первый ходит Игрок {p1}')
# else:
#     print('Первый ходит БОТ')
# while cnt > 0:
#     if flag:
#         n1 = hod(p1, cnt)
#         cnt -= n1
#         print(f'{p1} взял {n1} конфет. Осталось {cnt}. Ход переходит Боту')
#         flag = 0
#     else:
#         if 54 >= cnt > 29:
#             n2 = cnt - 29
#         elif cnt <= 28:
#             n2 = cnt
#         else:
#             n2 = random.randint(1, 28)
#         cnt -= n2
#         print(f'Бот взял {n2} конфет. Осталось {cnt}. Ход переходит игроку.')
#         flag = 1
# if flag:
#     print(f'БОТ забирает все конфеты')
# else:
#     print(f'Игрок {p1} забирает все конфеты')

# 3. Создайте программу для игры в ""Крестики-нолики"".
# Пример интерфейса:
#
#    |   | 0
# -----------
#    |   |
# -----------
#    | X |
# Ввод можно реализовать через введение двух чисел (номеров строки и столбца).
import random
print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1, 10))


def draw_board(desk):  # рисуем игровое поле
    print("-" * 13)
    for i in range(3):
        print("|", desk[0 + i * 3], "|", desk[1 + i * 3], "|", desk[2 + i * 3], "|")
        print("-" * 13)


def take_input(player_smb):  # просим у юзера координату для символа
    valid = False
    while not valid:
        player_inp = input('Куда поставим ' + player_smb + '?')
        if player_inp.isdigit():
            if 9 >= int(player_inp) >= 1:
                player_inp = int(player_inp)
                if str(board[player_inp - 1]) not in "XO":
                    board[player_inp - 1] = player_smb
                    valid = True
                else:
                    print('Эта клетка уже занята!')
            else:
                print('Некорректный ввод. Введите номер поля от 1 до 9:')
        else:
            print('Некорректный ввод. Введите номер поля от 1 до 9:')


def check_win(desk):  # проверяем победу
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for el in win_coord:
        if desk[el[0]] == desk[el[1]] == desk[el[2]]:
            return desk[el[0]]
    return False


def tic_tac_toe(game_field, fl):
    cnt = 0
    win = False
    while not win:
        draw_board(game_field)
        if fl:
            take_input("X")
            fl = False
        else:
            take_input("O")
            fl = True
        cnt += 1
        if cnt > 4:
            tmp = check_win(game_field)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if cnt == 9:
            print("Ничья!")
            break
    draw_board(game_field)


# запуск
flag = random.randint(0, 1)
if flag:
    print('Первым ходит Х')
else:
    print('Первым ходит O')
tic_tac_toe(board, flag)

input("Нажмите Enter для выхода!")

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# s = input('Введите строку:')
# k = 1
# s_n = ''
# i = 0
# while i < len(s):
#     while (i + 1) < len(s) and s[i] == s[i + 1]:
#         k += 1
#         i += 1
#     s_n += str(k) + s[i]
#     k = 1
#     i += 1
# print(s_n)
