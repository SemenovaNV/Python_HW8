from os import path
import csv

def delete():
   
    name = input('Введите фамилию абонента, которого хотите удалить: ')
    file = 'Phonebook.csv'
    if path.exists(file):
        newBook = []
        with open (file, 'r', encoding = 'utf-8') as text:
            count = False
            text_csv = text.readlines()
            text_csv = [line.rstrip() for line in text_csv]
            for i, v  in enumerate(text_csv):
                if name in v:
                    text_csv.pop(i)
                    print('Данные из телефонного справочника в были удалены')
                    count = True
            if not count: print('В телефонном справочнике таких данных нет')
            print(text_csv)
            newBook = text_csv

        with open(file, 'w', encoding='utf-8', newline='') as csvfile:
                fieldnames = ['id', 'first_name', 'last_name', 'number_phone']
                csv_writer = csv.DictWriter(csvfile, lineterminator="\r", fieldnames=fieldnames)
                listData = [{
                    'id': row.split(",")[0], 
                    'first_name': row.split(",")[1], 
                    'last_name': row.split(",")[2], 
                    'number_phone': row.split(",")[3]
                } for row in newBook
                ]
                print(listData)
                for rowData  in listData:
                    csv_writer.writerow(rowData)