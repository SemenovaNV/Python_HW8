import csv

def create_bd():
    with open('Phonebook.csv', 'w', newline='', encoding='utf-8') as phonebook:
        csv_writer = csv.writer(phonebook, delimiter=',')
        csv_writer.writerow(['id', 'first_name', 'last_name', 'number_phone'])
        csv_writer.writerow(['1', 'Иванов', 'Петр', '111111'])
        csv_writer.writerow(['2', 'Петров', 'Иван', '222222'])
        csv_writer.writerow(['3', 'Смирнова', 'Мария', '333333'])

create_bd()
