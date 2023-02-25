def ask_user():
    last_name = input('Enter your surname: ')
    first_name = input('Enter your name: ')
    phone_number = int(input('Enter your phone: '))
    return last_name, first_name, phone_number


def save_to_file(data: tuple, file, mode='a'):
    data_str = ' '.join(map(str, data))
    with open(file, mode, encoding='utf-8') as fd:
        fd.write(f'{data_str}\n')


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    headers = ['Surname', 'Name', 'Phone']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))
    return list_contacts


def read_file_to_list(file):
    with open(file, 'r', encoding='utf-8') as fd:
        lines = fd.readlines()
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(line)
    print(list_contacts)
    return list_contacts


def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'Surname', '2': 'Name', '3': 'Phone'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts


def ask_search():
    print('How do you want to do search?')
    search_param = input('1 - Surname, 2 - Name, 3 - Phone: ')
    what = None
    if search_param == '1':
        what = input('For search enter a surname: ')
    elif search_param == '2':
        what = input('For search enter a name: ')
    elif search_param == '3':
        what = input('For search enter a phone: ')
    return search_param, what


def search_contact_to_modify(list_contacts: list):
    surname = input('Enter surname: ')
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    for contact in list_contacts:
        if contact[0] == surname and contact[1] == name and contact[2] == phone:
            return contact


def modify_contact(file, list_contacts, cont):
    copy_contact = list(cont)
    list_contacts.remove(cont)
    print('What infor do you want to modify?')
    choice = input('1 - surname, 2 - name, 3 - phone: ')
    if choice == '1':
        copy_contact[0] = input('Enter new surname: ')
    elif choice == '2':
        copy_contact[1] = input('Enter new name: ')
    elif choice == '3':
        copy_contact[3] = input('Enter new number: ')
    list_contacts.append(copy_contact)
    with open(file, 'w', encoding='utf-8') as file:
        for i in list_contacts:
            line = ' '.join(i) + '\n'
            file.write(line)


def delete_contact(file, list_contacts, person):
    list_contacts.remove(person)
    with open(file, 'w', encoding='utf-8') as file:
        for i in list_contacts:
            line = ' '.join(i) + '\n'
            file.write(line)


def main_menu():
    file_contacts = 'file.txt'
    while True:
        user_choice = input('1 - add new contact,\n '
                            '2 - search contact,\n 3 - see the directory,\n 4 - modify existent contact,\n'
                            '5 - delete contact,\n 0 - exit\n Enter here: ')
        if user_choice == '1':
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            for i in read_file(file_contacts):
                for j in i:
                    print(i.get(j), end=' ')
                print()
        elif user_choice == '4':
            a_list = read_file_to_list(file_contacts)
            cont = search_contact_to_modify(a_list)
            modify_contact(file_contacts, a_list, cont)
        elif user_choice == '5':
            a_list = read_file_to_list(file_contacts)
            person = search_contact_to_modify(a_list)
            delete_contact(file_contacts, a_list, person)
        elif user_choice == '0':
            print('Bye for now')
            break


if __name__ == '__main__':
    main_menu()
