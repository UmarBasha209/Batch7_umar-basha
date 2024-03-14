# DAY 4

#----->While Loop
#----->Break using while loop

#eg:1
# 1.Iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<=30:
    if i==27:
        break
    print(i)
    i+=1

#2.
i=20
while i<=30:
    print(i)    o/p=20,21,22,23,24,25,26
    i+=1
    if i==27:
        break


# 3.
i=20
while i<=30:          o/p=20,21,22,23,24,25,26,27
    print(i)
    if i==27:
        break
    i+=1


i=20
while i<=30:
    if i==27:
        print(i)   o/p=27
        break
    i+=1


#!---> continue
#---> eg:1
i=20
while i<=30:
    i=i+1
    if i==27:              o/p=20,21,22,23,24,25,26,28,29,30
        continue
    print(i)
'''
#! eg:5
# while to iterate from 12 to 22
#find the sum of all numbers
'''
i=12
sum=0
while i<=22:
    sum=sum+i
    i+=1
print("sum of number is:",sum)
'''
#! eg:6
# find the average of value from 20 to 25
'''
i=20
avg=0
sum=0
while i<26:
    sum=sum+i           
    i+=1
    avg=(sum/6)
print("avg of value:",avg)


i=20
sum=0
count=0
while i<=25:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
'''
    
    
#!---> Nested for Loop
# eg:1
'''
for i in range(1,3+1):
    for j in range(1,4+1):
        print(i,j)
'''
#Eg:2
#* * * *
#* * * *
#* * * *
#* * * *
'''
for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()

rows=int(input("enter the rows: "))
cols=int(input("enter the cols: "))
for row in range(rows):
    for col in range(cols):
        print(row,end=" ")
    print()


sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum,end=" ")
    print()
'''


#! to print stars in right angled triangle
'''
for row in range(0,6):
    for col in range(0,row):
        print("*",end=" ")    o/p:right angle triangle
    print()

for row in range(0,7):
    for col in range(row,7):
        print("*",end=" ")   o/p:reverse right angle
    print()


for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row==0 or row==5-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")     0/p:square
    print()

'''
'''
  #       *
  #     * * *
  #    * * * *
  #   * * * * *


for row in range(0,5):
    for col in range(0,6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
'''
*
* *
*   *
*    *
* * * *
'''
'''
for row in range(0,6):
    for col in range(0,6):
        if(col==0 or (row==0 and col==0) or (row==1 and col==1) or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5 and col==5) or (row==6 and col==6)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()  
        
'''

#---> List
#---> Datatypes
# primary

#Number--> int,float complex
#string
#Boolean
#None

#Collection
#List
#Tuple
#Set
#Dictionary


#?---->List
#1. if the collection of elements sre sorounded by sqaure brackets,it is considered to be list
#!eg:
#l1=[4,7,9,9089, "hello", 7+9j, [8,9,0]]

# * charactristics of list
#1.list have to be sorrounded by[]
#2.it is mutable(the elements in the list are changable)
#3.every element inside list is indexed
#4.the element inside the list will be ordered format
#5.it can hold duplicate values
#6.its heterogenous

# to access the elements in list
lst1=[1,4,1,7,89.7,75,"p","i"]
#print(11)


#--> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value
# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

'''
#---> Positive indexing
lst1=[1,4,1,7,89.7,75,"p","i"]
print(lst1[0])
print(lst1[4])
print(lst1[20]) ----->error

#---> Negative indexing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[-1])
print(lst1[-5])

#?---> Slicing
lst1=[1,4,1,7,89.7,7.5,"p","i"]
#lst1[start_index:end_index:step]

print(lst1[0:4])
print(lst1[6:8])

lst1=[1,4,1,7,89.7,7.5,"p","i"]
print(lst1[3:6])
print(lst1[:5])
print(lst1[0:7:2])
'''
'''
# trail=int(input())
lst1=[1,4,1,7,89.7,7.5,"p","i"]
#print(lst1[-4:-1])
print(lst1[-1:-4])    ---->[]
print(1st1[-7:-1:2])
'''
#! To insert ot add element inside list
# append()-> used to add elelement at last position of list
lst1=[1,4,1,7,89.7,7.5,"p","i"]
 11= [9, 8, 0, 6]
 11.append("car")
print(11)





    
