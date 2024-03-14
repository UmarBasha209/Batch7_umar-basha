
# ! Eg:3
#  Take values of length and breadth of a
# from user and check if it is square or not
'''
length = int(input("enter length: "))
breadth = int(input("enter breadth: "))
if (length == breadth):
    print("It is a square ")
else:
    print("Not a square")
'''
          
# Eg:4
#python program to check whether the
#given integer is a multiple of both 5 and 7
'''
a=int(input("Enter a number:"))
if(a%5==0 & a%7==0):
    print("Yes")
else:
    print("No")
'''

#Eg:5
# write a program to accept the cost price of a bike
# road tax to be paid
# according to the following criteria:


 # cost price(in Rs)  Tax
 # >100000             15%+ discount 6%
 #  <100000   5%
'''
price=int(input("enter the price: "))
total=0
if price>=100000:
    discount=price*(6/100)
    value=price-discount
    amount=value*(15/100)
    total=value+amount
else:
    tax=price*(5/100)
    total=price+tax
print(" the on road cost of bike is: ",total)
'''

#Eg:6
# Accept the age of 4 pepole and display the oldest one
'''
a=int(input("enter first person age: "))
b=int(input("enter second person age: "))
c=int(input("enter third person age: "))
d=int(input("enter fourth person age: "))
if(a>b and a>c and a>d):
    print("a is oldest")
elif(b>a and b>c and b>d):
    print("b is oldest")
elif(c>a and c>b and c>d):
    print("c is oldest")
elif(d>a and d>b and d>c):
    print("d is oldest")
'''


# ! -----> Short hand if else
# Eg:1
'''    
a = 9
b = 60
if a>b:
     print("a")
else:
     print("b")
'''
#rules
#1.) statement inside the if condition have to be present at first
#2.) elif cannot be used in short hand if else
#3.) Always it have to end with else

# print("A") if a>b e;lse print("B")

# Eg:2
# A school has following rules for grading system:
# a.Below 25-F
# b.25 to 45 -E
# c. 45 to 50-D
# d. 50 to 60-C
# e. 60 to 80-B
# f. 45 Above 50-A
'''
mark=int(input("Enter mark: "))
if mark>=80 and mark<=100:
    print("A")
elif mark>=60 and mark<80:
    print("B")
elif mark>=50 and mark<60:
    print("C")
elif mark>=40 and mark<50:
    print("D")
else:
    print("Fail")
'''

'''
# ! code to check the given char is vowel or consonent
char=input("enter the char: ")
# if char =="a"char=="e" or char=="i" or char=="o" or char=="u"
# print ("is a vowel")
# else: print("its consonent")

# ? or

str1="umarfaruk"
if char in str1:
    print("vowel")
else:
    print("consonent")
    '''
 #! Short hand if else
   #  char=input("enter the char")
    #str1="umarfaruk"
    #print("vowels") if char in str1 else print("consonents")

#!--> elif ladder using short jhand if else
# Eg:!
#? find greatest among 3 variables using short hand if el;se
#a=8
#b=5
#c=9
# print("A is greater") if a>b and a>c else print("B is greater")
# if b>a and b>c else print("c is greater")


# !---> Looping
#looping can be implemented using
# for loop
# while loop

#--> for loop
# for loop is used for iteration, if we know the number of the times the loop have to run
# ?it is used to iterate thr iterables eg(strinh, list, tuple,etc..)

# todo--> Syntax for loop


#for | syntax in c
#for(i=0;i<10;i++){
 #   printf("hello");
#}

 #! for syntax in python
 #for userdefined_variable in range(start,end,step): default set value is 1
 
 # statement
 # statement
 # statement

 #?Eg:1
 # to print the value from 1 to 10 using for loop
'''

for i in range(0,10): #(n, n-1)
    #print(i)
      print("hello")
'''
#?Eg:2
'''

for val in range(15,30,2):
    print(val)
'''

#?Eg:3
'''
# to decrement the value

for val in range(10,0,-1):
    print(val)

for i in range(10,0,-2):
    print(i)
for val in range(10,0,1):
    print(val)#no output
  '''

#? Eg:4
#! print the output of 7th multiplication table fron 21 to 43
 #method1
    #for i in range(3,10+1):
   # print('7','x',i,'=',i*7)
#method2
    #ans="7x{}={}"
    #print(ans.format(i,i*7))      

# method3
#for i in range(1,10+1):
  #  print(f"7x{i}={i*7}")

#? Eg:5
# Break statement---> used to teerminate the loop
'''
for val in range(1,10):  o/p:1,2,3
    if val ==4:
        break
    print(val)
'''
#? Eg:6
'''
for val in range(1,10):      o/p:1,2,3,4,5,6
        print(val)
        if val==6:
            break
'''
#? Eg:7
'''
for val in range(1,10):        o/p:6
    if val==6:
        print(val)
        break
'''
#! continue
#Eg:1
'''
for val in range (1,10):
    if val==6 or val==7:
        continue
    print(val)
'''
'''
for val in range(1,30):
    if val==6 or val==9 or val==22:
        continue
    print(val)
'''
 #! practise problems
 #? print the even number b/w 20 to 40
'''
for val in range(15,47,1):
    if val %2==0:
        print(val)
'''
#!-----> While loop
# while is used when we do not knpw the number of times the loop have to run
# to iterate the non iterable elements while loop is used

# todo syntax

# initialisation
# while condition
# statement
# incre or decre

#! Eg:1
# to iterate number from 1 to  10

i=0
while i<11:
    print(i)
    i=i+1

# for loop practise
# write a program to display sum of odd numbers and even
# numbers that fall b/w
# 12 and 37(including both numbers)

# Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432


1 Eg:1
# to iterate numbedr from 1 to 10
# i = 0
# while i<11:
# print(i)
# 1=1+1 # OR I+=1
LE-318 DUDEKULA USMAN
15:50
#1st answer
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)
    if dist_cat_a == dist_cat_b:
        return "Mouse C"
    elif dist_cat_a < dist_cat_b:
        return "Cat A"
    else:
        return "Cat B"
# Example usage
print(catAndMouse(1, 2, 3))  # Output: Cat B

#  2nd answer
num = 8
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

# 3rd answer
sum_even = 0
sum_odd = 0
for num in range(12, 38):
LE-318 DUDEKULA USMAN
15:51
for num in range(12, 38):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)

# 4th answer
n1 = 123
total = 0
while n1 > 0:
    digit = n1 % 10
    total += digit
    n1 //= 10
print("Sum of digits of the number:", total)
#5th answer
n1 = 234
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("Reverse of the given number:", reverse)





















   

  
