# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

              #---->DAY-7

#Eg:1

# d1={'Ten':10,'Twenty':20,'Thirty':30}
# d2={'Thirty':30,'fourty':40,'fifty':50}
# d1.update(d2)
# print(d1)

#Eg:2
#set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
# c=0
# flag=0
# for i in range(3):
#     c=c+1
#     if c==1:
#         for i in set1:
#             if i in set2 or i in set3:
#                 flag=1
#                 break
#     if c==2:           
#         for i in set2:
#             if i in set1 or i in set3:
#                 flag=1
#                 break
#     if c==3:
#         for i in set3:
#             if i in set2 or i in set1:
#                 flag=1
#                 break
# if flag==0:
#     print("disjoint")
# else:
#    print("joint")
    
#Eg:3
# lst1 = ["M", "na", "i", "Ke"]
# lst2 = ["y", "me", "s", "lly"]
# l3=[]
# for i in range(len(lst1)):
#     ans=lst1[i]+lst2[i]
#     l3.append(ans)
# print(l3)

#using while Loop
# i=0
# while i<len(lst1):
#     l3.append(lst1[i]+lst2[i])
#     i+=1
# print(l3)

# Hacker rank---> caesar cipher
# ! Functions
# Function is a block of code which is used to a perform a specific functionality
# Function can be created using def keyword

#? Function has 3 parts
# function declaration
# function defanation
# function call

#!Eg:1
# def greet():  #
#     print("welcome to python")
# greet()

#!Eg:2
# def adding():
#     a=4
#     b=6
#     c=9
#     d=a+b+c
#     print(d)
# adding()
# adding()


#! Eg:2
#? Function with parameter
# def greeting(name):
#     print("welcome",name)
    
# for val in range(3):
#     username=input("enter the name: ")
#     greeting(username)


#! Eg:3
def profile(name,age,place):
    print(name,age,place)
profile("umar",209,"EEE")
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

# 3.)Wrire a code print the 8th fibanochi number
