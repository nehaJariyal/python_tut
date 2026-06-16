# class  is a blue print  for object 
# decorater  allow us to wrap another function  in  order  to   extend  the behavior of the  wrapped  function  without permanently modifying  it 

class Student:
    def __init__(self, name, marks):
        self.name =name
        self.marks= marks
    @staticmethod                      #  decorater  
    def hello():
        print("hello")
        
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avrage score  ",sum/3)
        
s1= Student("tony stark",[90 ,70,79])
s1.get_avg()
s1.hello()

#  important  opps  
#  four piler of opps 


# abstraction 

# hidden the implemetation  detail  of a class  and only  showing  the essential feature  to the user
#  hide unnessary thing  like A  car  we know only cluch  break  acessltor we dont know   internal process 

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch=False
        
    def start(self):
       self.clutch = True
       self.acc = True
       print("car started  ")
       
car1 =Car()
car1.start()

# encapuslation 
# wrapping  data and function into a single unit object 


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def credit(self, amt):
        self.balance += amt
        print("Rs.", amt, "was credited")
        print("Total balance =", self.get_bal())

    def debit(self, amt):
        self.balance -= amt
        print("Rs.", amt, "was debited")
        print("Total balance =", self.get_bal())

    def get_bal(self):
        return self.balance


account1 = Account(1000000, 1001001)

account1.credit(100000)
account1.debit(100)



# delete key word  use for delete  object properties or object itself 

class Sutdents:
    def __init__(self, name):
        self.name = name
        
s1 = Sutdents("neha")
print(s1.name)
# del s1.name
print(s1.name)
        #  how to  make private data  (self.__bank_account_password )  we can assess 
class Account_bank:
    def __init__(self, acont_no , account_pass):
        self.bank_account_no = acont_no
        self.__bank_account_password =account_pass
        
detl1 =Account_bank(123456,"Admin@123")
print(detl1.bank_account_no)
print(detl1.__bank_account_password)

class Person:
    __name = "neha"
    
    def __hello():
        print("hello")
        
p1 = Person()

print(p1.__name)
