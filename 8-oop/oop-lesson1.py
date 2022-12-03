'''
class Calc:
    #method = function
    #proparety = atribute

    def sum(self,x,y):
        print(x,y)
    # this sum belong to Calc not to python
    #self belong to the class ist variable and you can give any name
    def mul(self,x,y):
        print(x*y)

    def __init__(self,name):
        print(f'Welcome {name}')



c1 =Calc('Mahmoud')
#c1.sum(3,4)
#c1.mul(3,4)
'''

class Student:
    # def add_student(self): to make adding student easier we use __init__
    def __init__(self,name):
        print(f'welcome {name}')
        self.marks=[]
    def add_marks(self,mark):
        self.marks.append(mark)
        #print(self.marks)
    def get_avg(self):
        avg=sum(self.marks)/len(self.marks)
        print(avg)




ahmad=Student("ahmad")
ahmad.add_marks(50)
ahmad.add_marks(60)
ahmad.get_avg()




























