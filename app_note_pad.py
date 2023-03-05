from note_pad_function import Note

def app():
    is_continue = True

    while (is_continue):
        note_Pad = Note()
        print("Выберите действие: \n\
        1 Создать заметку \n\
        2 Просмотреть список заметок \n\
        3 Открыть заметку \n\
        4 Выйти \n")
        select = input()
        if select == "1":
            note_Pad.add_note()
        if select == "2":
            note_Pad.print_notes()
        if select == "3":
            note_Pad.select_note()
        if select == "4":
            is_continue = False