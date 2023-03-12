import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Текст заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\n Добро пожаловать в 'Заметки'. Список функций:\n\n1 - вывод всех заметок из файла\n"
          "2 - добавление заметки\n3 - удаление заметки\n4 - редактирование заметки\n"
          "5 - выборка заметок по дате\n6 - показать заметку по id\n7 - выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текcт: ')
    else:
        return text


def goodbuy():
    print("Пока, пока")