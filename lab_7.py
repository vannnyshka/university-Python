#Вариант 14: Продовольственные товары (наименование, отдел магазина, дата выпуска, срок хранения) Отсортировать по алфавиту названия и вывести товары
#с неистекшим сроком хранения
from abc import ABC, abstractmethod
import datetime
import time
import json


class AbstractArray(ABC):

    @abstractmethod
    def __del__(self):
        print('Deleted class example.')

    @abstractmethod
    def print(self):
        pass


class Products(AbstractArray):

    def __init__(self):
        self.list_of_products = []
        self.num_of_nice_products = 0

    def __del__(self):
        return super().__del__()

    def fillProduct(self, n):
        for i in range(n):
            self.list_of_products.append({
                'name': checkForString(input('Enter product name: ')),
                'department': checkForString(input('Enter department of the store: ')),
                'life': checkForInt(input('Enter shelf life (months): ')),
                'date': datetime.date(2021, checkForInt(input('Enter the month of receipt of the product: ')), \
                                      checkForInt(input('Enter the day of receipt of the product: '))).timetuple(),
                'today': datetime.date.today().timetuple()
            })

    def edit_list(self):
        products.print()
        temp = input("What do you want to do? (delete/add) ")
        if temp == 'delete':
            n = int(input("Which item you want to delete? "))
            del self.list_of_products[n - 1]
            products.print()
        elif temp == 'add':
            n = int(input("How much item you want to add? "))
            products.fillProduct(n)
            products.run()
            products.print()

        if int(input("Want to edit your list? 0 - no, 1 - yes ")) == 1:
            return products.edit_list()

    def run(self):
        i = 0
        number = len(self.list_of_products)
        while i < number:
            if self.list_of_products[i]["date"][1] < self.list_of_products[i]["today"][1] and \
                self.list_of_products[i]["date"][2]+self.list_of_products[i]["life"] < self.list_of_products[i]["today"][2] :
                i+=1
            else:
                del self.list_of_products[i]
                number -= 1

        self.list_of_products = sorted(self.list_of_products, key=lambda item: item['name'])

    def recordToFile(self):
        str_to_record = ''
        for i in range(len(self.list_of_products)):
            str_to_record += (f'Name: {self.list_of_products[i]["name"]} '
                              + f'Department of the store: {self.list_of_products[i]["department"]} '
                              + f'Shelf life: {self.list_of_products[i]["life"]} '
                              + 'Date: ' + time.strftime("%d %b", self.list_of_products[i]["date"]) + '; ')
        json.dump(str_to_record, open(f'A:\python\laba7.txt', 'w'))

    def print(self):
        super().print()
        for i in range(len(self.list_of_products)):
            print('\n' + f'Name: {self.list_of_products[i]["name"]}\n'
                  + f'Department of the store: {self.list_of_products[i]["department"]}\n'
                  + f'Shelf life: {self.list_of_products[i]["life"]}' + '\n'
                  + 'Date: ' + time.strftime("%d %b", self.list_of_products[i]["date"]))


def checkForInt(data):
    if data.isdigit():
        return int(data)
    else:
        data = input("Enter number!\n")
        return checkForInt(data)


def checkForString(data):
    if not data:
        data = input('Enter current name!\n')
        return checkForString(data)
    else:
        return data


products = Products()
products.fillProduct(checkForInt(input('Number of products: ')))
products.run()
products.print()
if checkForInt(input("Want to edit your list? 0 - no, 1 - yes ")) == 1:
    products.edit_list()
products.recordToFile()