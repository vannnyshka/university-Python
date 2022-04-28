#a1/N, a2/N, … 
from abc import ABC, abstractclassmethod, abstractmethod #Шаблоны класса
import time
 
class AbstractArray(ABC):
 
    @abstractmethod
    def __init__(self):
        pass
 
    @abstractmethod
    def __del__(self):
        print("Deleted class example.")
 
    @abstractmethod 
    def print(self):
        pass
 
    @abstractmethod
    def create(self):
        pass
 
class Array(AbstractArray): #Массив через шаблон
 
    def __init__(self, array = []):
        super().__init__()
        self.array = array
 
    def create(self, n):  #Глобальное создание массива
        super().create()
 
        input_data = []
 
        for i in range(n):
            input_data.append(input("a[]: "))
 
        input_type = input("Введите тип элементов массива a[]: ") #Определение типа введенного массива
 
        if input_type == 'float':
            float_num = createFloat(input_data, n)
            self.array = completeArray(float_num, n)
 
        if input_type == 'int':
            int_num = createInt(input_data, n)
            self.array = completeArray(int_num, n)
 
        if input_type == 'str':
            self.array = completeArray(input_data, n)
 
    def print(self):  #Отображение массива 
        super().print()
        print("Array:", self.array)
 
    def __del__(self):  #Деструктор массива
        return super().__del__()
 
 
def createFloat(input_data, n): #Создание массива
    for i in range(n):
        input_data[i] = float(input_data[i])
    return input_data
 
def createInt(input_data, n):
    for i in range(n):
        input_data[i] = int(input_data[i])
    return input_data
 
def completeArray(array, n):
    for i in range(n):
        if type(array[i]) == str:
            temp_ = float(array[i])
            temp_ /= n
            array[i]= str(temp_)
        else:
            array[i] /= n    
    return array
 
n = int(input("n: "))
temp = Array([])
temp.create(n)
temp.print()