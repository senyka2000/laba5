import os
import csv

def print_opt():
    """
    Выводит на экран доступные функци
    """
    print("count - количество файлов в директории")
    print("edit - редактировать словарь")
    print("sort - сортировать по ключу ")
    print("save - записать изменения в словарь")
    print("select - выборка из словаря")
    print("show - показать словарь")

def print_data(data):
    """
    Выводит весь массив в консоль
    :param data лист
    """
    for row in data:
        print(row)


def print_room_number(data):
    """
    Выводит только те строки, где номер комнаты больше 110
    :param data лист
    """
    print_data(row for row in data if int(row["age"]) > 13)


def count_file(path):
    """
    Подсчитывает кол-во файлов в пути, который задал пользователь
    :param path путь до директории
    :return cnt кол-во файлов
    :return 0 если неверный путь
    """
    try:
        return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    except:
        print("Неверный путь")
        return 0


def change_csv(data):
    """
    Изменяет данные в data
    :param data лист
    """
    row = int(input("Строка для редактирования: "))
    item = input("Введите ключ, который надо поменять: ")
    val = input("Поменять на: ")
    if row >= 0:
        data[row][item] = val
        print("Успешно изменено")
    else:
        print("Строка не может быть отрицательной")


def sort_csv_data(data):
    """
    Сортирует массив по определённому ключу
    :param data лист
    """
    key = input("Сортировать по ключу: ")
    try:
        data.sort(key=lambda item: item[key])
        print("Сортировка прошла успешно")
    except:
        print("Такого ключа не существует")


def save_csv(data):
    """
    Перезаписывает файл .csv формата на то, что было сохранено в data
    :param data массив
    """
    names = ['#', 'nickname', 'breed', 'age']
    with open("data.csv", "w") as csvfile:
        wrt = csv.DictWriter(csvfile, delimiter=";", fieldnames=names, quotechar="|", lineterminator="\r")
        wrt.writeheader()
        for row in data:
            wrt.writerow(row)
    print("Данные успешно записаны в файл")


def main():
    """
    Главная функция с вариативами для пользователя
    """
    print_opt()
    data = []
    with open("data.csv", "r") as cf:
        file = csv.DictReader(cf, delimiter=";")
        for row in file:
            data.append(row)
    while True:
        temp = input("Выберите операцию: ")
        if temp == 'count':
            print("Найдено файлов: {}".format(count_file(input("Путь: "))))
        elif temp == 'edit':
            change_csv(data)
        elif temp == 'sort':
            sort_csv_data(data)
        elif temp == 'save':
            save_csv(data)
        elif temp == 'select':
            print_room_number(data)
        elif temp == 'show':
            print_data(data)
        else:
            break


if __name__ == '__main__':
    main()
