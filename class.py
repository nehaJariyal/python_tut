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