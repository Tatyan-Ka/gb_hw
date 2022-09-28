# -*- coding: utf-8 -*-
from tkinter.filedialog import askopenfilename
import file_work


def menushka():
    while True:
        print(f'1 - Показать все записи\n'
              f'2 - Экспорт в файл\n'
              f'3 - Импорт из файл\n'
              f'4 - Добавить запись в справочник\n'
              f'0 - Выход из программы\n')
        n = int(input(f'Введите номер действия:'))
        if n == 0:
            print('До свидания. Хорошего дня!')
            break
        elif n == 1:
            file_work.show_all('phone_book.txt')
        elif n == 2:
            count_f = file_work.count_rows('phone_book.txt')
            s = input(f'Введите число строк для экспорта от 1 до {count_f} (по умолчанию экспортируются все '
                      f'строки)')
            form1 = int(input(f'Выберите формат экспорта (1 - в строку, 2 - в столбик):'))
            if s == '':
                cnt_str = count_f
            else:
                cnt_str = int(s)
            file_work.export_file(cnt_str, form1)
        elif n == 3:
            form2 = int(input(f'Выберите формат импорта (1 - в строку, 2 - в столбик):'))
            file_work.import_file(askopenfilename(), form2)
        elif n == 4:
            file_work.append_rec('phone_book.txt')
