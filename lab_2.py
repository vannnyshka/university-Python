#Заданы значения, найти h. 
import math

x, y, z = 2.444, 0.869e-2, -130

class Primer: 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def schet(self): #Функция подсчет
        firstpart = ((self.x ** (self.y+1))+ math.exp(self.y-1))/(1+self.x*(math.fabs(self.y-math.tan(self.z))))*(1+math.fabs(self.y-self.x))
        secondpart = (math.fabs(self.y-self.x)**2)/2
        thirdpart = (math.fabs(self.y-self.x)**3)/3
        h = firstpart + secondpart - thirdpart
        self.h = h
        
    def showOtvet(self): #Функция вывода ответа
        print("h = ", self.h)

print(" --------------- ")
otvet = Primer(x, y, z)
otvet.schet()
otvet.showOtvet()
print(" --------------- ")