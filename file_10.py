   #DAy-10

# polymorphism in classes
# we can acheive polymorphism in 2 ways
# 1.) Method overloading ---> it is not possible in python
# 2.) Method overriding

#! Method riding
#* polymorphism in classes
#?Eg:1
# class bank:
#     def ratio(self):
#         print("all banks has repo rate")
# class SBI(bank):
#     def ratio(self):
#         print("SBI rate is 8%")
# class IOB(bank):
#     def ratio(self):
#         print("IOB rate is 9.5%")
# i=IOB()
# i.ratio()
# s=SBI()
# s.ratio()


#? EG:2
# class USA:
#     def language(self):
#         print("English")
#     def capital(self):
#         print("Washington DC")
# class India(USA):
#     def language(self):
#         print("None")
#     def capital(self):
#         print("New delhi")
# I=India()
# I.language()
# I.capital()

# EG:3
# polymorphism using objects

# c1,c2 ---> c1=print(c1),print(c2)
# #f1,f2

#* Eg:4
# class c1:
#     def f1(self):
#         print("class 1")
# class c2:
#     def f1(self):
#         print("class2")
# obj1=c2()
# obj2=c1()
# def display(a):
#     a.f1()
# display(obj1)
# display(obj2)

#* changing the functionality of bulit in function
# class shooping:
#     def __init__(self,l1):
#         self.items=l1
        
#     def __len__(self):
#         length=len(self.items)
#         return length
# s=shooping([1,2,3,4,5])
# print(len(s))

# a=9
# b=6
# print(a+b)
# print(a.__add__(b)) #? dunder method or mafic method

# int()
# print(a.__sub__(b))

#! --> Method overloading
#! Eg:1
# class suming:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# s=summing()
# s.add(4,5,1) #!---> ERROR

#Eg:2
# class summing:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print(a)
# obj=summing()
# obj.add(2)
# obj.add(3,4)
# obj.add(1,2,3)
            
#! ----> Abstraction
# the process of hiding the implimentation details is abstraction

#? Eg:1

# from abc import ABC,abstractmethod
# class shapes(ABC):
#     @abstractmethod
#     def sides(self):
#         print('All shapes have sides except circle')
# class triangle(shapes):
#     def triangle_sides(self):
#         print("3 sides")
#     def name(self):
#         print("i am triangle")
#     def sides(self):
#         pass
# class square(shapes):
#     def square(self):
#         print("4 sides")
#     def sides(self):
#         pass
# tr=triangle()
# tr.triangle_sides()
# tr.name()

#! Rules to define abstract class1
# 1.) Abstract class cannot be instantiated
# 2.) From abc import ABC, abstract method
# 3.) Subclass the normal class with ABC
# 4.) Convert the normal method inside the abstract class to abstract method
# 5.) all the child classes have to be present inthe child classes

#!Eg:2
#* super()---> used to access the parent class method from child class method
# from abc import ABC,abstractmethod
# class c1(ABC):
#     @abstractmethod
#     def m1(self):
#         print("this is abstract class")
# class c2(c1):
#     def m2(self):
#         print(" i am child")
#     def m1(self):
#         pass
# class2=c2()
# class2.m2()

#*Eg:3
# from abc import ABC, abstractmethod
# class password(ABC):
#     @abstractmethod
#     def pwd(self):
#         pswd="umar209$"
# class login(password):
#     def validate(self,name,password):
#         if super().pwd()==password:
#             print("welcome",name,'!!')
#             print("Login succesfull")
#         else:
#             print("please check the password")
#     def pwd(self):
#         pass
# Login=login()
# name=input("enter the name: ")
# pwd=input("enter the password: ")
# Login.validate(name,pwd)

#***! Encapsulation
# class car:
#    __name="BMW" #private variable
# c1=car()
# print(c1.name) #error
# c1.name="Audi"
# print(c1.name)  #errpr

#* ---> EG:2
#? Accessing private date outside the class
# class c1:
#     __phone='9391626025'
#     def display(self):
#         print(self.__phone)
# c=c1()
# c.display()

#*---> Eg:3
#? declare private method
# class class1:
#     def __m1(self):  #private method
#         print("i am private method")
#     def __init__(self):
#         self.__m1
# c=class1()
# #c.__m1() #error


#? nested class
# class class1:
#     class class2:
#         name="umar"
#         def display(self):
#             print(self.name)
# obj=class1()
# obj.obj1.display()   


# ! ---> TASK
# 1.) Write the code for the below tasks using function
#     d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
for val in d1:
    if d1[val]==min(d1.values()):
        print(val)
for val in d1:
    if d1[val]==max(d1.values()):
        print(val)
for val in d1:
    if val.startswitch('s') or val.startswitch('s'):
        print(val)



#     a.) Find the min and max priced product
#     b.) Find the product starts with 's' and 'S'
# 2.) Find the n = 67, is strong number or not
