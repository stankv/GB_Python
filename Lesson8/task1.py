# Телефонный справочник

# Исправлена ошибка в реализации ф-ии read_records(), предложенной на семинаре - id считается правильно,
# только когда 1 <= id <= 9. Для двузначных id бралась только 1-я цифра.

from os import path, system

system('cls')

file_base = "base.txt"
all_data = []
id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


# Считывание данных из базы
def read_records():
    global all_data, id

    with open(file_base) as f:
        all_data = [i.strip() for i in f]
        if not all_data:
            return all_data
        if all_data != ['']:    # файл существует, и он не пустой
            sub_all_data = all_data[-1].split()
            id = int(sub_all_data[0])
        return all_data


# Отображение всего содержимого (всех контактов) базы данных
def show_all():
    if not all_data or all_data == ['']:
        print("Empty data")
        return False
    else:
        print(*all_data, sep="\n")
        return True


# Добавление новой записи (контакта)
def add_new_contact():
    global id
    array = ['Last Name', 'First Name', 'Middle Name', 'Phone number']
    string = ''
    for i in array:
        string += input(f"Enter {i}: ") + " "
    id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f'{id} {string}\n')


# Поиск записи (контакта)
def search_contact():
    what_search = input("Search: ").strip()
    if what_search != '':
        flag = True
        for record in all_data:
            if what_search in record:
                print(record)
                flag = False
        if flag:
            print("Data not found")
    else:
        print("Data don't entered for search")


# Изменение записи (контакта)
def modify_contact():
    global all_data
    if not show_all():
        return
    modify_id = input(
        "Enter the ID of the contact you want to modify: ").strip()
    if modify_id.isdigit() and int(modify_id) > 0 and len(all_data) >= int(modify_id):
        sub_all_data = all_data[int(modify_id) - 1].split()
        play = True
        while play:
            answer = input("What you want to change:\n"
                           "1. Last Name\n"
                           "2. First Name\n"
                           "3. Middle Name\n"
                           "4. Phone Number\n"
                           "5. Exit from Change Contact\n"
                           ">>> ")
            if answer in "1234":
                sub_all_data[int(answer)] = input("Enter change: ").strip()
                all_data[int(modify_id) - 1] = " ".join(sub_all_data)
                with open(file_base, "w", encoding="utf-8") as f:
                    for j in all_data:
                        f.write(j + '\n')
            elif answer == "5":
                play = False
            else:
                print("Uncorrect input. Try again!\n")
            print()
    else:
        print("Uncorrect ID!")


# Удаление записи (контакта)
def delete_contact():
    global all_data, id

    if not show_all():
        return
    del_id = input("Enter the ID of the contact you want to delete: ").strip()
    if del_id.isdigit() and int(del_id) > 0 and len(all_data) >= int(del_id):

        all_data.pop(int(del_id) - 1)
        for i in range(int(del_id) - 1, len(all_data)):    # пересчет id в записях
            sub_all_data = all_data[i].split()
            change_id = sub_all_data[0]
            all_data[i] = all_data[i].replace(change_id, str(i + 1))

        with open(file_base, "w", encoding="utf-8") as f:
            for j in all_data:
                f.write(j + '\n')
        id -= 1
        print("Contact deleted!")
    else:
        print("Uncorrect ID!")


# Импорт базы данных
def import_base():
    global file_base

    file_name = input("Enter filename (with extension): ").strip()
    if not path.exists(file_name):
        print(f"File {file_name} not found")
    else:
        file_base = file_name
        print("Import success!")


# Экспорт базы данных
def export_base():
    file_name = input(
        "Enter filename (without extension) for export: ").strip()
    if not path.exists(file_name):
        with open(f'{file_name}.txt', "w", encoding="utf-8") as f:
            for record in all_data:
                f.write(f'{record}\n')
        print("Export success!")
    else:
        print("A file with the same name already exists!")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Modify a record\n"
                       "5. Delete a record\n"
                       "6. Import a base\n"
                       "7. Export the base\n"
                       "8. Exit\n"
                       ">> ")
        if answer == "1":
            show_all()
        elif answer == "2":
            add_new_contact()
        elif answer == "3":
            search_contact()
        elif answer == "4":
            modify_contact()
        elif answer == "5":
            delete_contact()
        elif answer == "6":
            import_base()
        elif answer == "7":
            export_base()
        elif answer == "8":
            print("Bye!")
            play = False
        else:
            print("Try again!\n")
        print()


main_menu()
