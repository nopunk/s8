def input_name():
    return input("Введите имя: ")

def input_surname():
    return input("Введите фамилию: ")

def input_patronumic():
    return input("Введите отчество: ")

def input_phone():
    return input("Введите номер телефона: ")

def input_address():
    return input("Введите адрес: ")

def create_contact():
    name = input_name()
    surname = input_surname()
    patronumic = input_patronumic()
    phone = input_phone()
    address = input_address()
    return f"{name} {surname} {patronumic} {phone}\n{address}\n\n"

def add_contact():
    contact = create_contact()
    with open("phonebook.txt", "a", encoding="UTF-8") as f_w:
        f_w.write(contact)

def print_phonebook():
    with open("phonebook.txt", "r", encoding="UTF-8") as f_r:
        contacts_str = f_r.read()
        list_contacts = contacts_str.rstrip().split("\n\n")
    for i, contact in enumerate(list_contacts, 1):
        print(i,contact+"\n")

def find_contact():
    search = input("Введите данные для поиска: ")
    print(
        "Возможные варианты поиска:\n"
        "1. По имени\n"
        "2. По фамилии\n"
        "3. По отчеству\n"
        "4. По телефону\n"
        "5. По адресу\n"
        )
    var = input("Выберите вариант поиска: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод!")
        var = input("Выберите вариант поиска: ")
        i_var = int(var) - 1
    with open("phonebook.txt", "r", encoding="UTF-8") as f_r:
        contacts_str = f_r.read()
    list_contacts = contacts_str.rstrip().split("\n\n")
    for contact in list_contacts:
        contact_lst = contact.split()
    #print(contact_lst)
    if search in contact_lst[i_var]:
       print(contact)


def ui():
    with open("phonebook.txt","a", encoding="UTF-8"):
        pass
    choise = "0"
    while choise != "4":
       print(
            "Возможные варианты действий:\n"
            "1. Добавление нового контакта\n"
            "2. Вывод данных на экран\n"
           "3. Поиск контакта\n"
           "4. Выход из программы\n"
              )
    choise = input("Выберите вариант действия: ")
    while choise not in ("1","2","3","4"):
            print("Некорректный ввод!")
            choise = input("Выберите вариант действия: ")
        # match choise:
        # case "1":
        # add_contact()
        # case "2":
        # print_phonebook()
        # case "3":
        # find_contact()
        # case "4":
        # print("Всего доброго!")
    if choise == "1":
            add_contact()
    elif choise == "2":
            print_phonebook()
    elif choise == "3":
            find_contact()
    else:
            print("Всего доброго!")

ui()