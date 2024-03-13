'''
---> Variables
one variable=no.of variables
   #a,b,c=9,8,7,6
   #print(a,b,c)


      #a,b=c=7,8
      #print(a)
      #print(b)   o/p: 7  ,8   ,(7,8)
      #print(c)


      #a=b,c=4,2
      #print(a,b,c)   o/p:(4,2),4,2


         '''


a=7
b=5
temp=a  #temp=7
a=b     #a=b
b=temp  #b=7
print(a)
print(b)

  #Eg:2
a=a+b   #a=12
b=a-b   #b=12-7=5
a=a-b    #a=12-5=7
print(a,b)

a=a*b    #a=7*5=35
b=a/b    #b=35/7=5.0
a=a/b    #a=35/5=7.0
print(a,b)

a=7
print(a)
print(id(a))


#id()--->used to find the memory address of the variable
a=7
b=8
print(id(a))
print(id(b))

#---->Keywords
#keywords are reserved words which provides special meaning to
#compiler or interpretor

import keyword
#print(keyword.kwlist)
#print(len(keyword,kwlist))
#print(type(keyword,kwlist))

#top check if the string is keyword or not
#print(keyword.iskeyword("sid")) #false
if=8
print(if)

 #A variable is consider to be constant when it is defines
#in caps
  #a=78 # a is variable
# A=78 #A is constant
























   
   
