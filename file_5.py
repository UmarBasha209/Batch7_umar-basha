     #DAY 5
#! ----> common function for list
'''
l1=[6,7,8,9,0]
print(len(l1))
print(max(l1))
print(min(l1))
'''
'''
l1=[6,8,9, "p","u"]
print(max(l1))   # ---> error
print(min(l1))   #--->error
'''

#l1=[6,7,8,9,0,8.89,-5,0.78]
#print(min(l1))  #-5


#l1=[6,7,8,9,0,8.89,-5,0.78]
# index() ---> to get index value of specific element
#print(l1.index(9))

#l1=[6,7,8,9,0,8.89,-5,0.78]
# count()--->how many num of times an element is repeated
# print(l1.count(6))

#! some functions which is specifically used for list
# To add element inside the list
#? insert(index_value,element)--> to add element at specific index position
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2,"cars")
#print(l1)

#? To delete element from list
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#pop()--> last element will be deleted
#l1.pop()
#print(l1)

# pop(index_value)---> used to delete element at specific index
#l1.pop(4)  #4 is index value
#print(l1)

# remove(element)----> used to delete element directly
#l1.remove(8.89)
#print(l1)

#" clear()--> to complete delete all element in the list
#l1.clear()
#print(l1)

#del --> to delete the list
#del l1
#print(l1)

#?---> join 2 lists
#l1=[9,0,8]
#l2=["p","o","t",34]
#print(l1+l2)


# or
# extend() --> to combine 2 lists
#l1.extend(l2)
#print(l1)

# ?--->copy()
#l1=[6,6,6,7,8,9,0,8.89,-5,0.78]
#l2=l1.copy()
#print(l2)
#print(l1)

#print(id(l1))
#print(id(l2))

#! diff b/w shallow copy and deep copy
# shallow copy
#import copy
#l1=[8,9,0,[5,6],[3,2,1]]
#l2=copy.copy(l1)
#l1.append(209)
#print(l1)
#print(l2)


#* deep copy --> used to copy the list with nested list
#import copy
#l1=[8,9,0,[5,6],[3,2,1]]
#print(l1[-1][1]) #--> to index nested list

#l2=copy.deepcopy(l1)
#l1.append('209')
#print(l1)
#print(l2)

#? sort --> arrange elements in list in ascending or descendhing order
#l1=[9,7,45,0,-6,5,-12]
#l1.sort() # to arrange in ascending order
#print(l1)


#l1.sort(reverse=True) # to sort in descending order
#print(l1)

#l1=['z','i','o','m',9]
#l1.sort()
#print(l1) #--> error

#? list constructor
#list() #--> to conver other collection datatype to list
#l3=((6,9,8))
#print(list(l3))

#14=(8,9)
#print(list(14))

#! --> nested list

#l1=[8,9,[0,8,4],["u","n",'y'],[8,'t']]
#print(l1[-2][1]) #-->0

#print(l1[1:4])
#print(11[1:-1])

#? to delete "t" from l1
# l1[-1].remove('t')
#print(l1)

#? comdine these["p","o",'j'],[9,'u'] lists in l1 to["h","r",'s',3,'g']

#l1[-2].extend(l1[-1])
#l1.pop(-1)
#print(l1)

# ! ----> Tuple

#1.) tuple have to be surrounded by ()
#2.) The element inside tuple are not changable
#3.) The element inside tuple are indexed
#4.) The element will excuted in order
#5.) It is heterogenous
#6.) It allow duplicate element


#* eg:
# t1=(8,4,6,2,5.78,[9,0],(6,8),"hii",9+6j)
# print(t1)
# print(type(t1))

#? indexing, slicing are all same as list

        #? ways to create tuple
# l1=(8)
# print(type(l1)) #int

# l1=(8,)
# print(type(l1))

#t1=8,9
#print(type(t1)) # tuple

# t2=8,
# print(type(t2)) #tuple

# len(), min(),max(),index(),count() ---> all same as list

# to add  element inside tuple ---> cannot add
# cannot delete any element from tuple


# * jon 2 tuples

#t1 = (8, 9, 0)
#t2 = (6, 7, 8)
#print(t1 + t2)

# To add all element inside list and tuple
#sum()
#l1 = (8, 9, 7, 6)
#print(sum(l1))


# * sort tuple
#t1 = (8, 9,0, 89, 12)
#print(tuple(sorted(t1)))
#print(tuple(sorted(t1, reverse=True)))

# * Iterate list and tuples

# Iterate based on Elements

#l1 = [9, 8, 0, 6, 5]
#for i in l1:
    #print(i)

# * Iterate based on Index value
#l1 = [9, 8, 0, 6, 5]
#for i in range(0,5):
    #print(i)


# ! ---> Strings
'''
s1 = 'o'
print(type(s1))


s1 ="u"
print(type(s1))


s1 = "hello world"
# * To access string
print(s1)
'''
# Indexing and slicing --> same as list and tuple
# print(s1[0:5])
'''
# --> len(), min(),max(), index(),count()
s1 = "hello world"
print(len(s1))
print(max(s1))
print(min(s1))

#ord() ---> used to find the ASCII value of character
s1 = 'u'
print(ord(s1))
'''

# Functions of string
##s1 = "hello world"


# ? to convert all character to upper case
#print(s1.upper())

#? to convert to lower case
#s1 = "HFREDiou"
#print(s1.lower())



# ? strip() ---> to eliminate the space in beginning and end of string

#s1 = " where are you?"
#print(s1.lstrip())
#print(s1.lstrip())
#print(s1.strip())




# Split() --->
#s1 = " where are you ?"
#print(s1.split())
#print(s1.split("r"))

#s1 = " where are you ?"
#print(s1.count('e'))


# * replace() ---> to replace a specific char in the string
#s1 = "Where are you?"
#print(s1.replace('r', '&&'))

# Swapcase () ---> to convert



# Swapcase () ---> to convert
#s1 = "HEY there "
#print(s1.swapcase())

'''
# * title() --> to write the string in format of title
s1 = 'never giveup'
print(s1.title())


# * capitalize() --> 1st character of string will be converted to capital
s1 = 'never giveup'
print(s1.capitalize())

'''
# * Join the strings
#s1 = " hello"
#s2 = 'world'
#print(s1+s2)


'''
s1 = how are you
i am fine
hey there
'''


# splitlines() --> used to split the string based on lines
#print(s1.splitline())

# * find() --> to find the index based on
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))
# * join() -->
#l1 = ["hey" ,"there"]
#print(" ".join(l1))
#print("$",join(l1))


#s1="welcome to all"
#print(s1.endswitch('1'))
#print(s1.startswitch('w'))
'''
s1 = "67"
print(type(s1))
print(s1.isdigit())
'''

# * print the string in reverse manner
#s1 = "Welcome to all"
#print(s1[::-1])

#! ---> Eg:1
# wap to find the number of lower case letters
#s1=" HEY where are YOU"
#count=0
#for i in s1:
    #if i.islower():
        #count+=1
#print("the total num of lower cases letters: ",count)

# ! ---> Eg:2 r--> "$"
#s1='restarter'
#s1="IMAGIN"
#print(s1.replace('r',"$"))

#fst=s1[0]
#bal=s1[1:]
#txt=bal.replace(fst,"$")


#---> Eg:3

s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop"
#characters=len(s1)
#print(characters)

#words=s1.split(" ")
#print((lenwords))
'''
sentences=s1.split('.')
for val in sentences:
    if val=='':
        print(sentences)
'''
space=0
for val in s1:
    if val ==" ":
        space=space+1
    print(space)


# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]


