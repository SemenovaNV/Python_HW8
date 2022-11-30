import csv

def search():
    search = input('Введите фамилию для поиска абонента: ')
    with open('Phonebook.csv', 'r', encoding='utf-8') as phonebook:
        reader = csv.reader(phonebook, delimiter=',')
        name = None
        for row in reader:
            if search == row[1]:
                return print(f'Данные по поиску {search} - {row[0]} {row[1]} {row[2]} {row[3]}')  
        if name:
            print(name)
        else:
            print(f'Абонента с фамилией {search} не найдено\n')
    
