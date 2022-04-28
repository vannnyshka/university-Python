x1, x2 =1, 2
class X: #Класс Х
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        
    def showX(self): #Виртуальный метод просмотра текущего состояния
        print("x1 = ", self.x1, " x2 = ", self.x2)
    
    def changeX(self): #Переустановки объектов базового класса в новое состояние
        self.x1 = int (input("Введите x1 = "))
        self.x2 = int (input("Введите x2 = "))
        
    def __del__(self):
        print("Вызвался деструктор")


class Y(X):
    def __init__(self, y):
        super().__init__(x1,x2)
        self.y=y
    
    def showXY(self): #Виртуальный метод просмотра текущего состояния
        print("x1 = ", self.x1, " x2 = ", self.x2, "y = ", self.y)
        
    def changeXY(self): 
        self.x1 = int (input("Введите x1 = "))
        self.x2 = int (input("Введите x2 = "))
        self.y = int (input("Введите y = "))
        
    def Run(self): #Функция подсчета
        print("Результат выражения: ", (self.x1-self.x2)/self.y)
        


print(" --------------- ")
temp=Y(X)
temp.changeXY()
temp.showXY()
temp.Run()
temp.changeX()
temp.showX()
temp.Run()
print(" --------------- ")
