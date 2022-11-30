import csv

def get_add_column():
    with open('Phonebook.csv', 'r', encoding='utf-8') as phonebook:
        file_reade = csv.reader(phonebook, delimiter = ",")
        # field_names = ['id', 'first_name', 'last_name', 'number_phone'] 
        # column_name = input ('Введите название нового столбца: ')
        # # for x in phonebook:
        # #     x[column_name] = '*'
        # field_names.append(column_name)
        # print(field_names)

    with open('Phonebook.csv', 'a+', newline='', encoding='utf-8') as phonebook:
        field_names = ['id', 'first_name', 'last_name', 'number_phone'] 
        column_name = input ('Введите название нового столбца: ')
        for x in phonebook:
            x[column_name] = '*'
        csv_writer = csv.writer(phonebook, delimiter=',')
        field_names.append(column_name)
        print(field_names)
        csv_writer = csv.DictWriter(phonebook, fieldnames=field_names)
        csv_writer.writerow(field_names)
        print('\nИзменения внесены\n') 

     