from datetime import datetime as dt
from view import get_action

def general_log(mode):
    time = dt.now().strftime('%H:%M')
    with open ('log.txt', 'a', encoding='utf-8') as file:
        file.writelines(f'Операция {mode} выполнена в {time}\n')
        
