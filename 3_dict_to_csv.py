"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv
    #jober = [{"name":"Filipp", "age": 31, "job": "logistical"},
            #{"name":"Vlad", "age": 32, "job": "builder"},
           # {"name":"Vova", "age": 33, "job": "saler"},
           # {"name":"Dima", "age": 30, "job": "engineer"}]
    #print(jober)
    #print(jober[2]["name"])
    
    #w = csv.writer(open("jobs.csv", 'w', encoding="utf-8"))
    worker = [{"name":"Filipp", "age": 31, "job": "logistical"},
            {"name":"Vlad", "age": 32, "job": "builder"},
            {"name":"Vova", "age": 33, "job": "saler"},
            {"name":"Dima", "age": 30, "job": "engineer"}]

    with open('worker3.csv', 'w', encoding="utf-8") as f:
        #writer = csv.DictWriter(f, fieldnames=worker[0]) #заголовок вариант 1 берет fieldnames из словаря worker 0 значение
        fields = ["name", "age", "job"] #заголововки вариант 2 прописываем сами
        writer = csv.DictWriter(f, fields, delimiter=",")
        writer.writeheader() #
        writer.writerows(worker) #записать строку



if __name__ == "__main__":
    main()
