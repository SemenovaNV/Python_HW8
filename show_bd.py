import csv

def show_bd():
    with open('Phonebook.csv', encoding='utf-8') as phonebook:
        file_reade = csv.reader(phonebook, delimiter = ",")
        for row in file_reade:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]}') 
        