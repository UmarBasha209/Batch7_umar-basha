     #DAY-8
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number


#! eg:2
#? function with parameter 
# def greeting(name):a name is parameter
# print("welcome",name)

# for val in range(3):
# username=input("enter the name:")
# greeting(username_) # username is argument

#! EG:3
# def profile(name,age,place):
# txt="my name is {}. i am {} years old. i am from"
# profile("umar",209,"EEE")

#! EG:4
#! function with return statement

#def f1():
#z=8
#f1()
# print(z) #error

# def f1(a,b):
#     c=a*b
#  #   return # print(f1(6,8))
# obj=f1(6,8)
# obj=f1(4,6)

#def gracemark(object):
# print(object+4)
#gracemark(obj)
#gracemark(obj1)

# problem 112

# def palindrome(n):
#     string=str(n)
#     rev=str(n)
#     rev=str(n)[::-1]
#     if string==rev:
#         print(n,"palindrome")
#     else:
#         print("Not palindrome")
# a=int(input("enter the value: "))
# palindrome(a)



# positional args
# keyword ars
# default args
# variable args
# variable length args
# keyword variable length args


#*positional args
#? the position of parameter ahve to be same as position os arguments
#! eg:1
# def profile(name,phone,mark):
#     txt=" my name is {}.my phone number is {}. i got {} marks."
#     print(txt.format(name,phone,mark))
# profile(name="umar",mark=209,phone=9391626025)

 #* todo --> Exception of keyword args function
# def profile(name, phone, mark):
#     txt="My name is{}. My phone number{}. I got{} marks{}."
#     print(txt.format(name,phone,mark))

# profile(name = "shashank", mark=99, phone=9876543210) # Error
# profile(23166516521,name= "umar", mark=99) # error
#profile("umar",mark=98,phone=23166516521)


#* Default args
# the method of assigning the arguments to the parameter while declaring the function
#! Eg:1
# def profile(name,phone,place="kadapa"):
#     txt="my name is {}. my phone number is{}, i am from{}."
#     print(txt.format(name,phone,place))
    
# profile("umar",1236547890,)


#! eg:2
# def profile(name,phone,place="kadapa"):
#     txt="my name is {}. my phone number is{}, i am from{}."
#     print(txt.format(name,phone,place))
    
# profile("umar",1236547890,"guntur")





# Problem Statement – Given a string S(input consisting) of ‘*’ and ‘#’. 
# The length of the string is variable. The task is to find the minimum number of ‘*’ 
# or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
# and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
# Note : The output will be a positive or negative integer based on number of ‘*’ 
# and ‘#’ in the input string.

# (*>#): positive integer
# (#>*): negative integer
# (#=*): 0

# ! Exception
# def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
#     if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
#      txt="My name is{}. My phone number{}. I got{} marks{}."
#      print(txt.format(name,phone,place))
#     else:
#         print("You are not eligible to Signup")
# file("umar",123644977)

#!Eg:1
# to pass more then 1 arg to a parameter means we use variable length args
# to convert normal parameter to variable length param,add,to their prefix of parameter
# name="umar",'name2','name3'
# def profile(name):
#     for val in name:
#         print("my name is",val)
# profile("umar",'name2','name3')

#!Eg:2
# def profile(*name,age):
#     for val in name:
#         print("my name is",val,"may age is",age)
# profile("umar",'name2','name3',28)  # error----> age has no args

# def profile(age,*name):
#     for val in name:
#          print("my name is",val,"may age is",age)
# profile(209,"umar",'name2','name3')

#* keyword variable length args
# kwargs--> which is used to provide the args in the form of key value pair
#! Eg:1
# def price(**price_lst):
#     print(price_lst)
# price(shirt=1000,shoe=40000)

# d1={"a":100,"b":200,"c":300}
# d1=dict(a=100,b=200,c=300)
# print(d1)

# n=5
# {1:1,2:4,3:9,4:16,5:25}
# n=int(input("enter the number: "))
# def dict1(n):
#     d1={}
#     for val in range(1,n+1):
#         d1[val]=val**2
#     print(d1)
# dict1(5)

#!-----> object oriented programming
# the panadigms of object oriented programming are
#class
#objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# class is a blue print of an object
# l1=[1,2,3,4,5,6] 

#!Eg:1
# class c1:
#     name1="umar"
#     print(name1)
    
#!Eg:2
# class person:
#     name="umar"
# c=person() # c os object
#the process of creation of an object is called as instantiation
# print(c.name)
    
#Eg:3
# create of a method
# when the function is created with a class is called as method 

#! method without parameter
# class person:
#     def display(person): # it is a method
#         print("hello welcome to classes")
# p=person()
# p.display()

#? Eg:4
#! method with parameter
# class person:
#     def display(person,name,age):
#         print(name,age)
# p=person
# p.display("umar",19)

#? Eg:5
# class person:
#     name="sidhu"  #attributre of static variable
#     lname="T"
#     def first_name(self):
#         print(self.fname)
#     def full_name(self):
#         print(self.fname+" "+self.lname)
# p=person1()
# p.first_name()
# p.full_name

#? EG:6
# constructors 0---> init()
# this is a special method which has the ability to execute iteself without
# calling it manullay through the process of instantitation
# class profile:
#     def_init_(self):
#         print("hey")
# p=profile()
