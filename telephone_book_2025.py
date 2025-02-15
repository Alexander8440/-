import os


meny_tephone_book: list = [ # меню телефонного справочника

    'Показать все контакты',
    'Найти контакт',
    'Добавить контакт',
    'Удалить контакт',
    'Изменить контакт'
]

def open_contacs(): # функция открытия справочника
    with open('contacts.txt','a',encoding='UTF-8') as file: # создание текстового файла если его не было
        if os.stat('contacts.txt').st_size == 0: # проверка пустой файл или нет
            print('*'*30)
            print('Справочник пуст!!!') # говорит нам о том, что справочник пуст или его не существует
            print('*' * 30)
            show_meny() # представление меню
        else:
            show_meny() # представление меню

def show_meny(): # представление меню
    for number, item in enumerate(meny_tephone_book, 1): # нумерование меню
        print(number, item) # вывод на экран

def show_all_the_contacts():# просмотр контактов
    with open('contacts.txt','r',encoding='UTF-8') as file: # открытие файла на чтение
        show_cont = file.read().split() # чтение и преобразование файла в список
        for num, cont in enumerate(show_cont,1): # нумерация контактов
            print(num,cont) # вывод на экран

def search_for_contact(): # функция поиска контакта
    with open('contacts.txt','r',encoding='UTF-8') as file: # открытие файла для чтения
        contacs = list(file.read().split()) # чтение файла и преобразование его в список
        search_for_a_name = input('Введите имя для поиска: ') # ввод имени для поиска
        for cont in contacs: # итерация списка контактов
            for i in cont.split(':'): # итерация контакта
                if i == f'Имя-{search_for_a_name}': # условие при котором находится нужное имя
                    print(cont) # вывод на экран


def add_contact():# добавление контакта
    with open('contacts.txt','a',encoding='UTF-8') as file: # открытие файла на запись
        new_name = input('Введите имя: ') # ввод имени от пользователя
        new_number = input('Введите номер телефона: ') # ввод номера от пользователя
        new_comment = input('Напишите комментарий: ') # ввод комментария от пользователя
        file.write(f'{'Имя'}-{new_name}:{'Телефон'}-{new_number}:{'Комментарий'}-{new_comment}\n') # запись контакта
        print('Контакт успешно добавлен')
        file.close() # сохранение файла

def delete_contact():
    with open('contacts.txt','r+',encoding='UTF-8') as file: # окрытие файла для чтения
        contacs = file.read().split() # преобразование файла в список
        for num,cont in enumerate(contacs,1): # нумерация контактов
            print(num,cont)
        number = int(input('Выберите номер контакта который хотите удалить ')) # ввод номера от пользователя
        del contacs[number-1] # удаление по индексу
        print('Контакт успешно удален')
    with open('contacts.txt','w',encoding='Utf-8') as file: # открытие файла на перезапись
        for i in contacs: # итерация контактов
            file.write(f'{i}\n') # запись контактов
        file.close() # сохранение файла

def change_contact():
    with open('contacts.txt','r+',encoding='UTF-8') as file: # открытие файла на чтение и запись
        contacs = file.read().split()  # преобразование файла в список
        for num, cont in enumerate(contacs, 1): # нумерация контактов
            print(num, cont)
        number = int(input('Введите номер контакта который хотите редактировать: '))
        cont = contacs[number-1].split(':') # создание списка из контакта
        print(cont[0]) # вывод имени на экран по индексу
        new_name = input('Введите имя: ')
        cont[0] = new_name # изменение имени
        print(cont[1]) # вывод номера на экран по индексу
        new_numbers = input('Введите номер: ')
        cont[1] = new_numbers # изменение номера
        print(cont[2]) # вывод комментария на экран по индексу
        new_comment = input('Напишите комментарий: ')
        cont[2] = new_comment # изменение комментария
        contacs[number-1] = f'{'Имя'}-{cont[0]}:{'Телефон'}-{cont[1]}:{'Комментарий'}-{cont[2]}' # сохранение новых
        # данных
        with open('contacts.txt', 'w', encoding='Utf-8') as file:  # открытие файла на перезапись
            for i in contacs: # итерация контактов
                file.write(f'{i}\n') # запись контактов
            file.close() # сохранение файла


def start(): # функция начало программы
    print('#'*60)
    print('Здравствуйте! Хотите открыть телефонный справочник?')
    print('#' * 60)
    user_choice = input('Выберите да или нет: ') # выбор пользователя открыть справочник или нет
    if user_choice == 'да': # условие если пользователь выбрал "да"
        print('&' * 60)
        print('Добро пожаловать в телефонный справочник')
        print('&' * 60)
        open_contacs() # функция открытия справочника
        choice_of_a_item = input('Выберите пункт меню: ') # выбор пункта меню пользователем
        if choice_of_a_item == '1': # условие если выбрал просмотр контактов
            show_all_the_contacts()
        elif choice_of_a_item == '2': # условие если выбрал поиск контактов
            search_for_contact()
        elif choice_of_a_item == '3': # условие если выбрал добавление контакта
            add_contact()
        elif choice_of_a_item == '4': # условие если выбрал удаление контакта
            delete_contact()
        elif choice_of_a_item == '5': # условие если выбрал изменение контакта
            change_contact()
        print('@'*60)
        print('Спасибо за то, что воспользовались нашим справочником')
        print('@' * 60)
    else:
        print('Всего хорошего')

start() # старт программы