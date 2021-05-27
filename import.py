from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass
    
class Rectangle(Shape):
    def getArea(self):
        return 5*5
    
class Circle(Shape):
    def getArea(self):
        return 3.14*(5**2)
    
class CreatorShape:
    def getInstance(self,type):
        if(type=="Circle"):
            return Circle()
        elif(type=="Rectangle"):
            return Rectangle()
        else:
            return None
        
s = CreatorShape()
print(s.getInstance("Rectangle").getArea())