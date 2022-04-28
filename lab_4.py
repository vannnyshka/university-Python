#Если длина строки кратна 4, выделяем подстроку после последнего пробела
class string_class:
    def __init__(self):    #Инициализация класса
        self.String = ''
 
    def setter(self):       #Функция ввода строки
        self.String = input("Введите строку: ")
 
    def print(self):         #Функция вывода новой строки
        print("Введенная строка: ", self.String)
 
    def __del__(self):
        print("Вызвался деструктор")
 
 
def task():
    String_1 = ''
    obj = string_class()
    obj.setter()
    obj.print()
    if len(obj.String) % 4 == 0:
        print("длина строки кратна четырем")
        n = int (obj.String.rfind(" "))
        for i in range(0, len(obj.String), 1):
            if i > n:
                String_1 += obj.String[i]
 
    else:
        print("длина строки не кратна четырем")
    print(String_1)
 
 
task()