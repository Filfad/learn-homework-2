"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
     
    dt_now = date.today()
    yesterday = date.today()- timedelta (days=1)
    thirty_days_ago = date.today()- timedelta (days=30)
    print(f"{dt_now} {yesterday} {thirty_days_ago}")


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_string = "01/01/20 12:10:03.234567"
    dt_2_str = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    print (dt_2_str)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
