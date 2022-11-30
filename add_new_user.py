import csv

def append_user():
    with open('Phonebook.csv', 'r', newline='', encoding='utf-8') as phonebook:
        reader = csv.DictReader(phonebook)
        max_id = 1
        for row in reader:
            # print(row)
            # print(row['id'], type(row['id']))
            if max_id < int(row['id']):
                max_id = int(row['id'])
    # print(max_id)

    # reader['id'] = str(max_id + 1)
    with open('Phonebook.csv', 'a+', encoding='utf-8', newline='') as phonebook:
        fieldnames = ['id', 'first_name', 'last_name', 'number_phone']
        new_user ={}
        new_user['id'] = str(max_id + 1)
        new_user['first_name'] = input ('Введите фамилию: ')
        new_user['last_name'] = input ('Введите имя: ')
        new_user['number_phone'] = input ('Введите номер телефона: ')
        append_writer = csv.DictWriter(phonebook, fieldnames=fieldnames)
        append_writer.writerow(new_user)
        
       
        
        
    





    print('\nИзменения внесены\n') 