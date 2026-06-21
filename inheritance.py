# inheritance  when  one class drive the properties and  methods of another class
# sigle  level inheritance 

class Car:
    @staticmethod
    def start():
        print("car stated")
    @staticmethod
    def stop():
        print(" stop car ")
        
class TyoptaCar(Car):
    def __init__(self, name):
             self.name =name
             
car1= TyoptaCar("fortuner")
car2 = TyoptaCar("prius")

print(car1.start())

# multi level inheritance 

class Fortuner(TyoptaCar):
    def __init__(self, type):
        self.type = type
        
car3= Fortuner("diesel")
car1.start()

# multiple inheritance 

class A:
    varA= "welcome to class A"
class B:
        varB= "welcome to class B"
class C(A,B):
        varC= "welcome to class C"
c1=C
print(c1.varA)
print(c1.varB)
print(c1.varC)

# super
# super method is used to access method  of the parent  class 



class Car2:
    def __init__(self,type):
        self.type =type 
         
    @staticmethod
    def start():
        print("car stated")
    @staticmethod
    def stop():
        print(" stop car ")
        
# class TyoptaCar3(Car2):
#     def __init__(self, name):
#              self.name =name
#              super().type
             
# car5= TyoptaCar3("fortuner")
 
# print(car5.type)

        
        #  method 
        # static method   =>   no class no instance 
        #  class methods =>    class atribute 
        #  instanse method => where we can use istant methods 
        
        #  decorater 
        # @staticmethod
# @classmethod
# @property


class Student :
    def __init__(self , phy, chem ,eng):
        self.phy = phy 
        self.chem = chem 
        self.eng = eng 
        self.ppercentage = str((self.chem+self.eng+self.eng)/3)+"%"
        
stu1=Student(98,79,90)  
print(stu1.ppercentage)       