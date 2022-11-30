from view import get_action
from show_bd import show_bd
from search import search
from add_new_user import append_user
from add_column_bd import get_add_column
from change import change
from delete_bd import delete
import sys
from logger import general_log

def start():
    action = get_action()
    # print(action)
    if action == 1:
        show_bd()
    elif action == 2:
        search()
    elif action == 3:
        append_user()
    elif action == 4:
        get_add_column()
    elif action == 5:
        change()
    elif action == 6:
        delete()
    elif action == 7:
        sys.exit("Вы завершили работу с базой данных")     
    general_log(action)
