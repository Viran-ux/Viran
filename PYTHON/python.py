
        # CYBROM TOPICS IN PYTHON


'''
tokens 
       keyword
       String
       punctuation
       identifier
       literals
       operations
'''
'''
 type of operations
 object
 index 
 slicing
 range
'''

''' "Type of operations"

 Arithmetic operator
 assignment operator
 comparison operator
 Logical operator
 membership operator
 identity operator
 Bitwise operator
'''

''' frozenset

 list = [2,4,6,"DUBAI"]
 fs = frozenset(list)
 print(type(fs))
 print(id(fs))
 print(len(fs))
 
'''

''' THIS IS FOR RANGE

 x = range(10)

 print(x)

 print(type(x))
'''

''' EVEN NUMBER
 n = int(input("Enter a number :"))
 x = list(range(2,n+1,2))
 print(x)
 print(type(x))
'''

''' ODD NUMBER
 n = int(input("Enter a number :"))
 x = list(range(1,n+1,2))
 print(x)
 print(type(x))
'''

# x = range(-1,-11,-1)

# print(list(x))

# x = range(-1,-11,-2)

# print(list(x))


# x = range(1,10,-1)
# print(tuple(x))


'''
separation set 

 x = 10
 y = 20
 z = 30

 print(x,y,z,sep=' ')

'''

''' 
use of end
 print("hello",end=" ")
 print("hi")
 
'''


# x = int()
# print(x)
# print(type(x))

# x = float()
# print(x)
# print(type(x))

# x = complex()
# print(x)
# print(type(x))

'''

s1 = 'python'
s2 = 'language'

l = [s1,s2]
x = ','.join(l)

print(x)

'''

'''


s = "Hello,my name is jerry,i am 26 years old"
x = s.split(',')
print(x)

'''

'''
s = "apple#banana#pomegranate#mango"

x = s.split("#")
print(x)
'''

'''
s = "apple#banana#pomegranate#mango"

x = s.split("#",1)
print(x)
'''

'''
# list methods


l = [2,4,6,'viras','riyadh']

l1 = l.copy()
print(l1)
print(l)
print(id(l1),id(l))

'''
'''
l = [2,4,6,'viras','riyadh']

l.clear()
print(l)
print(id(l))

del l 
print(l)

'''

'''
l = [2,4,6,'viras','riyadh','java']

l.append(['delhi','vira'])
print(l)
'''

'''
l = [2,4,6,'viras','riyadh','java']

l.insert(2,"viras")
print(l)
'''

'''
l = [2,4,6,'viras','riyadh','java']

l.extend(['python','js'])
print(l)
'''

'''
l = [2,4,6,'viras','riyadh','java']

l.pop(3)
print(l)
'''

'''
x = eval(input("Enter an number :"))

print(x)
print(type(x))

'''

'''
d = {"x":10,"y":20,'Z':"30"}

d1 = d.copy()
print(d1)
print(id(d),id(d1)) 

'''
'''
d = {"x":10,"y":20,'Z':"30"}

d.clear()
print(d)
'''

'''

d = {"x":10,"y":20,'Z':"30"}

print(d.items())

'''

'''

d = {"x":10,"y":20,'Z':"30"}

print(d.popitem())
print(d)

'''

'''
l = ["x","y","z"]

d = dict.fromkeys(l,5000)
print(d)
'''

'''
l = ["python"]

d = dict.fromkeys(l,5000)
print(d)
'''

'''
l = 'virans'

d = dict.fromkeys(l)
print(len(l))
'''

'''
d = {"x":10,"y":20,"z":30}

d1 = d.setdefault("p",100)
print(d1)
print(d)
'''
# set = {10,20,30,'python'}

# set.add('java')
# print(set)

# l1 = [2,4,6,8]
# l2 = [1,3,5,7]
# set.update(l1,l2)
# print(set)

# set = {10,20,30,'python'}

# set.remove('python')
# print(set)
# set.discard('python')

# fs = frozenset({1,2,'python'})
# print(fs)
# print(type(fs))

# s = 'python'
# fs = frozenset(s)
# print(fs)
# print(type(fs))


# fs = frozenset({1,2,5}) 
# eval(input("Enter s Number :"))
# print(type(fs))


# fs = frozenset({1,2,3,4,5}) 
# fs2 = frozenset({4,5,6,7,8})
# print(fs.union(fs2))

# fs = frozenset({1,2,3,4,5}) 
# fs2 = frozenset({4,5,6,7,8})
# print(fs.intersection(fs2))

# fs = frozenset({1,2,3,4,5}) 
# fs2 = frozenset({4,5,6,7,8})
# print(fs.difference(fs2))

# fs = frozenset({1,2,3,4,5}) 
# fs2 = frozenset({4,5,6,7,8})
# print(fs.symmetric_difference(fs2))

# ELEMENTS NOT SAME

# fs = frozenset({1,2,3,4,5}) 
# fs2 = frozenset({4,5,6,7,8})
# print(fs.isdisjoint(fs2))

# fs = frozenset({1,2,3,4,5,6,7}) 
# fs2 = frozenset({1,2,3,4})
# print(fs2.issubset(fs))

# fs = frozenset({1,2,3,4,5,6,7}) 
# fs2 = frozenset({1,2,3,4})
# print(fs2.issuperset(fs))

# fs = frozenset({1,2,3,4,5,6,7}) 
# fs2 = frozenset({1,2,3,4})
# print(id(fs))
# print(id(fs2))


'''TYPE CASTING'''


# x = input("Enter any value")
# print(x)
# print(type(x))
# print(int(x))
# print(type(int(x)))


# x = int(input("Enter any value :"))

# print(x)
# print(type(x))
# print(str(x))
# print(type(str(x)))

# x = float(input("Enter an value :"))
# print(x)

# print(str(x))

# l = (1,2,3,4,5)

# x = list(l)
# print(x)

# EMPTY SET

# x = []

# print(x)
# print(type(x))

# l = list()
# print(l)
# print(type(l))

# x = []
# print(x)
# print(type(x))
# val = eval(input("Enter an Number :"))
# x.append(val)

# print(x[0])

# x[0] = 'java'
# print(x[0])
# x.remove('java')
# print(x)

# x = []
# print(x)
# print(type(x))
# val = eval(input("Enter an Number :"))
# x.append(val)

# print(x[0])

# x[0] = 'java'
# print(x[0])
# x.remove('java')
# print(x)

# del x
# print(x)


# d = {}
# d['name'] = 'viras'
# print(d)

'''
d = {}
d['name'] = 'viras'
print(d)

d['name'] = 'python'

print(d)

print(d['name'])
'''


# d = {}
# d['name'] = 'viras'
# print(d)

# d['name'] = 'python'

# print(d)

# print(d['name'])

# d.pop('name')
# print(d)

'''
x = int(input("Enter an Number :"))
 
if (x%2==0):
    print("Even")

print("THANKS)

'''
'''
x = int(input("Enter an Number :"))
if (x%2==0):
    print("Even")
else:
    print("Odd")
print("thanks")
'''


# f string is a better way to showcase a code

# x = int(input("Enter an number :"))

# if (x>0):
#     print("POSITIVE NUMBER")
# elif (x<0):
#     print("NEGATIVE NUMBER")
# elif (x==0):
#     print("EQUAL TO ZERO")

# x = int(input("Enter an number :"))

# if (x>=0):
#     print(f'given no {x} is positive')
# else:
#     print(f'given no {x} is not positive')


#  5 QUESTIONS  

'''QUE : TO PRINT GREATEST OF TWO NUMBERS'''

# Number1 = int(input("Enter An Number :"))
# Number2 = int(input("Enter An Number :"))

# if (Number1>Number2):
#     print("Number 1 is greater than number 2")
# else:
#     print("Number 2 is greater than number 1")

'''QUE : TO CHECK A PERSON IS A SENIOR CITIZEN OR NOT'''

# age = int(input("Enter an Number :"))

# if (age>=60):
#     print("SENIOR CITIZEN")
# else:
#     print("NOT A SENIOR CITIZEN")

'''QUE : TO CHECK THE YEAR IS A LEAP YEAR'''

# year = int(input("Enter An Number :"))

# if ( year % 4 ==0 and year % 100 !=0) or ( year % 400 == 0 ):
#     print("LEAP YEAR")
# else:
#     print("NOT A LEAP YEAR")


'''QUE : TO CHECK THAT THE STUDENT IS PASS OR FAIL'''

# grade = int(input("Enter an Number :"))

# if (grade>=33):
#     print("PASS")
# else:
#     print("FAIL")


'''QUE : TO CHECK TEMPERATURE IN FAHRENHEIT AND CELSIUS'''

# temp_1 = float(input("Enter the temperature :"))
# temp_2 = input("Enter unit (C or F) :")

# if (temp_2=='C'):
#     fahrenheit = (temp_1*9/5)+32
#     print(f"{temp_1}°C is {fahrenheit}°F")
# else:
#     celsius = (temp_1-32)*5/9
#     print(f"{temp_1}°F is {celsius}°C")



# n = int(input("Enter any value :"))
# if n>0:
#     print(f'given number {n} is positive')
# elif n<0:
#     print(f'given number {n} is negative')
# elif n==0:
#     print(f'given number {n} is zero')


"WHILE LOOP"

# n = int(input("Enter an Number :"))

# i = 1
# while(i<=n):
#     if i<n:
#         print(i,end=',')
#     else:
#         print(i)
#     i+=1




# i = 1
# while(i<=10):
#     if i<=10-1:
#      print(i,end=',')
#     else:
#        print(i)
#     i+=1



# sum = 0
# i = 1
# while(i<=10):
#     sum+=i
#     if i<=10-1:
#      print(i,end='+')
#     else:
#      print(i,end='=')
#     i+=1
# print(sum)


'''PATTERN TOTAL 14'''


# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print('*'*n)
#     i+=1

# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#  print('*'*i)
#  i+=1

# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#   print(' '*(n-i)+'*'*i)
#   i+=1


# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#   print(' '*(n-i)+'* '*i)
#   i+=1


# n = int(input("Enter an Number :"))

# i = 0
# while i<n:
#     print('*'*(n-i))
#     i+=1


# n = int(input("Enter An Number :"))

# i = 0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1

# n = int(input("Enter an Number :"))
 
# i = 0

# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1

# i-=2
# while i>=1:
#     print(' '*(n-i)+'* '*i)
#     i-=1

# n = int(input("Enter an Number :"))
# if n%2==0:

#     pass

# else:
#     n = n//2+1
#     i =1
#     while i<=n:
#         print(' '*(n-i)+'* '*i)
#         i+=1
#     i-=2
#     while i>=1:
#         print(' '* (n-i)+'* '*i)
#         i-=1