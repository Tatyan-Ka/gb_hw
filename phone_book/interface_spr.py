# -*- coding: utf-8 -*-
from tkinter.filedialog import askopenfilename
import file_work

def menushka():
    n = int(input(f'1 - Показать все записи\n'
                  f'2 - Экспорт в файл\n'
                  f'3 - Импорт из файл\n'
                  f'4 - Добавить запись в справочник\n'
                  f'0 - Выход из программы\n'
                  f'Введите номер действия:'))
    return n

def vybor(n):
    if n == 1:
        file_work.show_all('phone_book.txt')
    elif n == 2:
        count_f = file_work.count_rows('phone_book.txt')
        cnt_str = int(
            input(f'Введите число строк для экспорта от 1 до {count_f} (по умолчанию экспортируются все строки)'))
        form = int(input(f'Выберите формат экспорта (1 - в строку, 2 - в столбик:'))
        file_work.export_file(cnt_str, form)
    elif n == 3:
        form = int(input(f'Выберите формат импорта (1 - в строку, 2 - в столбик:'))
        file_work.import_file(askopenfilename(), form)
    elif n == 4:
        file_work.append_rec('phone_book.txt')