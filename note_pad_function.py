from datetime import datetime
import csv
import os
import shutil

# создание класса "Заметки"
class Note:

#Конструктор
    def __init__(self):
        self


# создание функции новой заметки
    def add_note(self):
# проверка на то, существует ли файл .csv если нет, создание
        if os.path.isfile("notes/file.csv") == False:
            headerlist = ({"name_note": [], "date_time_last_save": [], "text_note": []})
            with open("notes/file.csv", "w", newline="", encoding="utf-8") as file_note:
                d_writer = csv.DictWriter(file_note, delimiter=";",fieldnames=headerlist)
                d_writer.writeheader()
# создание новой заметки
        print('Введите имя новой заметки:')
        new_name_note = input()
        date_current = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('Введите текст заметки:')
        text_note = input()

        with open("notes/file.csv", "a", newline="", encoding="utf-8") as note:
            writer = csv.writer(note, delimiter=";")
            writer.writerow([new_name_note, date_current, text_note])
            print("Заметка успешно создана!\n")

# функция выводящая в консоль список заметок
    def print_notes(self):
        print('Список заметок:')
        with open("notes/file.csv", encoding="utf-8") as note_list:
            reader = csv.DictReader(note_list, delimiter=";")
            for row in reader:
                print(row["name_note"])
            print("\n")

# функция редактирования заметок
    def select_note(self):
        print("Введите имя заметки:")
        name = input()

        with open("notes/file.csv", encoding="utf-8") as line:
            self.number_line = None
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
# нахождение номера строки по названию
                if row["name_note"] == name:
                    self.number_line = i
                    print("Выберете действие с заметкой:\n1) Открыть заметку\n2) Изменить заметку\n3) Удалить заметку\n")
                    count = input()
# действие "чтение заметки"
                    if count == "1":
                        with open("notes/file.csv", encoding="utf-8") as csv_file:
                            csv_reader = csv.reader(csv_file)
                            rows = list(csv_reader)
                            print(rows[self.number_line + 1])
# действие "редактирование заметки"
                    if count == "2":
                        with open("notes/file.csv", encoding="utf-8", newline='') as source, open("notes/new_file.csv", "w", encoding="utf-8", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest,delimiter=';')
                            for line,rows in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(rows)
                                if line == self.number_line + 1:
                                    date_current = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                    print("Введите новый текст:")
                                    new_text = input()
                                    writer.writerow([row["name_note"], date_current, new_text])
                        shutil.copy2(r"notes/new_file.csv", r"notes/file.csv")
                        os.remove('notes/new_file.csv')
# действие"удаление заметки"
                    if count == "3":
                        with open("notes/file.csv", newline='') as source, open("notes/new_file.csv", "w", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest,delimiter=';')
                            for line,row in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(row)
                        shutil.copy2(r"notes/new_file.csv", r"notes/file.csv")
                        os.remove('notes/new_file.csv')
                        print("Заметка удалена\n")
# действие если нет пользователь ввёл не существующую заметку
            if self.number_line == None:
                    print("Замтека не найдена\n")