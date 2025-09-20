
        # CYBROM TOPICS IN PYTHON

        #'''CORE PYTHON'''



'tokens '


'''
keyword
String
punctuation
identifier
literals
operations
'''



'type of operations'
'''
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

'EVEN NUMBER'

'''
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

'''x = range(-1,-11,-1)

print(list(x))'''

'''x = range(-1,-11,-2)

print(list(x))'''


'''x = range(1,10,-1)
print(tuple(x))'''


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


'''
x = int()
print(x)
print(type(x))

x = float()
print(x)
print(type(x))

x = complex()
print(x)
print(type(x))
'''

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

'LIST METHODS'


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

'DICTIONARY METHODS'

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

'SET METHODS'

''
set = {10,20,30,'python'}

set.add('java')
print(set)
''

''
set = {10,20,30,'python'}
l1 = [2,4,6,8]
l2 = [1,3,5,7]
set.update(l1,l2)
print(set)
''


''
set = {10,20,30,'python'}

set.remove('python')
print(set)
set.discard('python')   # Tries to remove 'python' again (but it's already removed)
''

'FROZENSET'


'''
fs = frozenset({1,2,'python'})
print(fs)
print(type(fs))
'''


'''
s = 'python'
fs = frozenset(s)
print(fs)
print(type(fs))
'''


'''
fs = frozenset({1,2,5}) 
eval(input("Enter s Number :"))
print(type(fs))
'''


'''
fs = frozenset({1,2,3,4,5}) 
fs2 = frozenset({4,5,6,7,8})
print(fs.union(fs2))
'''


'''
fs = frozenset({1,2,3,4,5}) 
fs2 = frozenset({4,5,6,7,8})
print(fs.intersection(fs2))
'''


'''
fs = frozenset({1,2,3,4,5}) 
fs2 = frozenset({4,5,6,7,8})
print(fs.difference(fs2))
'''


'''
fs = frozenset({1,2,3,4,5}) 
fs2 = frozenset({4,5,6,7,8})
print(fs.symmetric_difference(fs2))
'''

# ELEMENTS NOT SAME

'''
fs = frozenset({1,2,3,4,5}) 
fs2 = frozenset({4,5,6,7,8})
print(fs.isdisjoint(fs2))
'''


'''
fs = frozenset({1,2,3,4,5,6,7}) 
fs2 = frozenset({1,2,3,4})
print(fs2.issubset(fs))
'''


'''
fs = frozenset({1,2,3,4,5,6,7}) 
fs2 = frozenset({1,2,3,4})
print(fs2.issuperset(fs))


'''
'''
fs = frozenset({1,2,3,4,5,6,7}) 
fs2 = frozenset({1,2,3,4})
print(id(fs))
print(id(fs2))
'''


'''TYPE CASTING'''


'''
x = input("Enter any value")
print(x)
print(type(x))
print(int(x))
print(type(int(x)))
'''


'''
x = int(input("Enter any value :"))

print(x)
print(type(x))
print(str(x))
print(type(str(x)))
'''

'''
x = float(input("Enter an value :"))
print(x)

print(str(x))
'''

'''
l = (1,2,3,4,5)

x = list(l)
print(x)
'''

'EMPTY SET'

'''
x = []

print(x)
print(type(x))
'''

'''
l = list()
print(l)
print(type(l))
'''

'''
x = []
print(x)
print(type(x))
val = eval(input("Enter an Number :"))
x.append(val)

print(x[0])

x[0] = 'java'
print(x[0])
x.remove('java')
print(x)
'''

'''
x = []
print(x)
print(type(x))
val = eval(input("Enter an Number :"))
x.append(val)

print(x[0])

x[0] = 'java'
print(x[0])
x.remove('java')
print(x)


del x
print(x)
'''


'''
d = {}
d['name'] = 'viras'
print(d)
'''

'''
d = {}
d['name'] = 'viras'
print(d)

d['name'] = 'python'

print(d)

print(d['name'])
'''


'''
d = {}
d['name'] = 'viras'
print(d)

d['name'] = 'python'

print(d)

print(d['name'])

d.pop('name')
print(d)
'''

'''
x = int(input("Enter an Number :"))
 
if (x%2==0):
    print("Even")

print("THANKS")

'''

'''
x = int(input("Enter an Number :"))
if (x%2==0):
    print("Even")
else:
    print("Odd")
print("thanks")
'''


'f string is a better way to showcase a code'

'''
x = int(input("Enter an number :"))

if (x>0):
    print("POSITIVE NUMBER")
elif (x<0):
    print("NEGATIVE NUMBER")
elif (x==0):
    print("EQUAL TO ZERO")
'''


'''
x = int(input("Enter an number :"))

if (x>=0):
    print(f'given no {x} is positive')
else:
    print(f'given no {x} is not positive')
'''


' 5 QUESTIONS ' 

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


'''required n even number'''

# i = 1

# while i<=5:
#     if i<5:
#         print(2*i,end=',')
#     else:
#         print(2*i)
#     i+=1

# sum = 0
# i = 1
# while i<=5:
#     sum+=i*2
#     if i<5:
#         print(2*i,end='+')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(sum)


# multi = 1
# i = 1

# while i<=5:
#     multi*=i*2
#     if i<5:
#         print(2*i,end='*')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(multi)

'''required as user'''

# n = int(input("Enter Number :"))

# i = 1
# while i<=n:
#     if i<n:
#         print(2*i,end=',')
#     else:
#         print(2*i)
#     i+=1

# n = int(input("Enter Number :"))

# i = 1
# sum = 0
# while i<=n:
#     sum+=i*2
#     if i<n:
#         print(2*i,end='+')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(sum)


# n = int(input("Enter Number :"))

# i = 1
# multi = 1
# while i<=n:
#     multi*=i*2
#     if i<n:
#         print(2*i,end='*')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(multi)

'''required n odd number'''

# i = 1
# while i<=5:
#     if i<5:
#       print(2*i-1,end=',')
#     else:
#       print(2*i-1) 
#     i+=1

# i = 1
# sum = 0
# while i<=5:
#     if (i<=5-1):
#         sum+=i*2.5
#         print(2*i-1,end='+')
#     else:
#         print(2*i-1,end='=')
#     i+=1
# print(sum)


# i = 1
# multi = 1
# while i<=5:
#     multi*=i*2-1
#     if (i<=5-1):
#         print(2*i-1,end='*')
#     else:
#         print(2*i-1,end='=')
#     i+=1
# print(multi)


'''required as user'''

# n= int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print(2*i-1)
#     i+=1

# n = int(input("Enter an Number :"))

# i = 1
# sum = 0
# while i<=n:
#     sum+=i*2-1
#     if (i<=n-1):
#         print(2*i-1,end='+')
#     else:
#         print(2*i-1,end='=')
#     i+=1
    
# print(sum)

# n = int(input("Enter an Number :"))

# multi = 1
# i = 1
# while i<=n:
#     multi*=i*2-1
#     if (i<=n-1):
#         print(2*i-1,end='*')
#     else:
#         print(2*i-1,end='=')
#     i+=1

# print(multi)





'''ARMSTRONG NUMBER'''

# '''armstrong number'''

# n = int(input("Enter an Number :"))

# digit=sum=0
# x = y = n
# while n>0:
#     n = n//10
#     digit = digit + 1
# while x>0:
#     lastdigit = x%10
#     sum = sum+lastdigit**digit
#     x = x//10
# if sum==y:
#  print(f'given number {y} is Armstrong')
# else:
#    print("NOT ARMSTRONG")

'''OR'''

# n = int(input("Enter An Number :"))

# sum = 0
# orig = n

# while n>0:
#     sum = sum + (n%10)*(n%10)*(n%10)
#     n//=10
# if (sum==orig):
#     print(f'the given number {orig} is ARMSTRONG')
# else:
#     print(f'the given number {orig} is not ARMSTRONG')


'''to count digits'''

# n = int(input("Enter an Number :"))
# x = n
# digit = 0
# while n>0:
#     n = n//10
#     digit = digit + 1
# # print("N",n,"Digit:",digit)
# print(f'total digit of given no {x} is {digit}')

'''OR'''

# n = (input("Enter an Number :"))

# print(f'total digit of given number {n} is {len(n)}')




'''PATTERN TOTAL 14'''

'1' 'PRINTED AS VALUE OF n times given '

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print('*'*n)
#     i+=1

'2' 'PRINTED AS VALUE OF i in increment order'

# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#  print('*'*i)
#  i+=1


'3' 'LEFT ANGLED TRIANGLE'

# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#   print(' '*(n-i)+'*'*i)
#   i+=1

'4' 'LEFT INVERTED'

# n = int(input("Enter an Number :"))

# i = 0
# while i<n:
#     print('*'*(n-i))
#     i+=1

'5' 'RIGHT ANGLED TRIANGLE'

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print('*'*i+" "*(n-i))
#     i+=1

'6' 'RIGHT INVERTED'

# n = int(input("Enter An Number :"))

# i = 0
# while i<n:
#     print(' '*i+'*'*(n-i))
#     i+=1

'7' 'HALF DIAMOND'

# n = int(input("Enter an Number :"))
# i = 1

# while i<=n:
#   print(' '*(n-i)+'* '*i)
#   i+=1

'8' 'FUll DIAMOND'

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1

# i-=2
# while i>=1:
#     print(' '*(n-i)+'* '*i)
#     i-=1



'9'  'HALF HOURGLASS'

# n = int(input("Enter an Number :"))
 
# i = 0

# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1

'10'  'FULL HOURGLASS'

# n = int(input("Enter an Number :"))

# i = 0
# while i<n:
#     print(' '*i+'* '*(n-i))
#     i+=1
# i-=2
# while i>=0:
#     print(' '*i+'* '*(n-i))
#     i-=1


'PASS'

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


'''FOR LOOP'''


# my_string = 'python'
# my_list = [1,2,3,'python','java']
# my_tuple = (1,2,3,4,'python','java')
# my_dict = {'name':'viras','age':'17'}
# my_set = {1,2,3,'python','java'}

# for i in my_string:
#     print(i)
# for i in my_list:
#     print(i)
# for i in my_tuple:
#     print(i)
# for k,v in my_dict.items():
#     print(k,'=',v)
# for i in my_set:
#     print(i)


'''ASCII VALUES FROM DIGITS TO ALPHABETS'''

# s = 'abcde'
# s1 = ''

# for i in s:
#    x = chr(ord(i)+5)
#    s1 = ''.join((s1,x))
# print(s1)


# x = 'a'

# print(ord(x))

# s1 = 'viras'
# s = 'indi'

# print(' '.join([s1,s]))

# s = 'abcde'
# s1 = ''

# for i in range(-1,-6,-1):
#     print(i)
#     x = s[i]
#     s1 = ''.join([s1,x])
# print(s1)

'''OR'''

# s = 'abcde'
# s1 = ''

# for i in range(-1,-(len(s)+1),-1):
#     print(i)
#     x = s[i]
#     s1 = ''.join([s1,x])
# print(s1)

    
'''PATTERNS USING FOR LOOP'''

'1' 'PRINTED AS VALUE OF i in increment order'

# n = int(input("Enter an number :"))

# for i in range(1,n+1):
#     print('*'* i)

'2' 'PRINTED AS VALUE OF n times given '

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     print('*'*n)


'3' 'LEFT ANGLED TRIANGLE'

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     print(' '*(n-i)+"*"*i)

'OR'

# n = int(input("Enter an number :"))

# for i in range(n-1,-1,-1):
#     print(' '* i+'*'*(n-i))


'4' 'HALF DIAMOND'


# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)


'5' 'FULL DIAMOND'

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     print(' '*(n-i)+'* '*i)

# for i in range(n-1,-1,-1):
#     print(' '*(n-i)+'* '*i)



'6' 'LEFT INVERTED TRIANGLE'

# n = int(input("Enter an Number :"))

# for i in range(0,n+1):
#     print('*'*(n-i))

'7' 'RIGHT INVERTED TRIANGLE'

# n = int(input("Enter an Number :"))

# for i in range(0,n+1):
#     print(' '*i+'*'*(n-i))

'8' 'HALF HOURGLASS'

# n = int(input("Enter an Number :"))
 
# for i in range(0,n+1):
#     print(' '*i+'* '*(n-i))

'9' 'FULL HOURGLASS'


# n = int(input("Enter an Number :"))


# for i in range(0,n):    
#     print(' ' * i + '* ' * (n - i))

# for i in range(2,n+1):
#     print(' ' * (n - i) + '* ' * i)



'''WHILE ELSE'''

'''IF WE DONT USE BREAK THE LOOP DOESN'T TERMINATE IT RUN'S INFINITELY'''

# atmpin = '1234'
# pin = (input("Enter an Number :"))

# while (atmpin == pin):
#     print('Welcome to atm process')
#     break 
# else:
#     print('please enter correct pin')


# n = int(input("Enter an Number :"))




'''CONTINUE'''

# i = 1
# while i<=n:
#     if i==5:
#         # print(i) '''IT MAKES THE LOOP INFINITE IF WE DON'T USE CONTIN'''
#         continue
#     else:
#         print(i)
#     i=i+1




'''PASS'''

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     if i==5:
#         pass
#         print("HELLO")

#     else:
#         print(i)
#     i=i+1


'''BREAK'''

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     if i==5:
#        break
#     else:
#         print(i)
#     i=i+1



'''CALCULATOR'''

# while True:
#     print("1.addition \n 2.substrction \n 3.multiplication \n 4.divisiion \n 5.off")

#     n = int(input("Enter the type of calculation:"))

#     x = (1,2,3,4)

#     if n in x:
#         p = float(input("Enter an Number 1 :"))
#         q = float(input("Enter an Number 2 :"))

#         if n==1:
#          print('addition =',p+q)
#         elif n==2:
#          print('substraction =',p-q)
#         elif n==3:
#          print('multiplication =',p*q)
#         else:
#          print('division',p/q)

#     elif n==5:
#       break
#     else:
#       print("please enter an valid option")




    
'''sum of a list of numbers entered by the user'''
 
# n1 = int(input("Enter an Number :"))

# l = []
 
# for _ in range(n1):
#     variable = float(input("Enter an Number :"))
#     l.append(variable)
# sum = 0

# for i in l:
#     sum+=i
# print(f'sum of {l} = {sum}')


'''right-angled triangle of numbers.'''

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


'''right-angled triangle of even numbers '''

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(2*j,end='')
#     print()

'''right-angled triangle of odd numbers.'''

# n = int(input("Enter an Number :"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(2*j-1,end='')
#     print()



'''right-angled triangle pattern of sequential numbers.'''

# n = int(input("Enter an Number :"))

# j = 1

# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(j,end=',')
#         j+=1
#     print()

'''right-angled triangle pattern of sequential even numbers.'''

# n = int(input("Enter an Number :"))

# j = 1

# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(2*j,end=',')
#         j+=1
#     print()

'''right-angled triangle pattern of sequential odd numbers.'''

# n = int(input("Enter an Number :"))

# j = 1

# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(2*j-1,end=',')
#         j+=1
#     print()


'''rectangle pattern of capital letters'''

# n = int(input("Enter an Number :"))


# for i in range(1,n+1):
#     j = 'A'
#     for _ in range(1,n+1):
#         print(j,end=' ')
#         j = chr(ord(j)+1)
#     print()

'''pyramid pattern of capital letters'''

# n = int(input("Enter an Number :"))


# for i in range(1,n+1):
#     j = 'A'
#     for _ in range(1,i+1):
#         print(j,end=' ')
#         j = chr(ord(j)+1)
#     print()

'''pyramid pattern of capital letters sequentially'''

# n = int(input("Enter an Number :"))
# j = 'A'
# for i in range(1,n+1):
    
#     for _ in range(1,i+1):
#         print(j,end=' ')
#         j = chr(ord(j)+1)
#     print()'''


'''FUNCTION'''


# def add(x,y):
#    z = x+y
#    return z
# p = int(input("Enter an Number :"))
# q = int(input("Enter an Number :"))

# result = add(p,q)
# print(result)
# print(result)
# print(result)

'''PASS USED IN FUNCTION'''

# def add():
#     pass
# add()
# print(add())


'''TYPES OF ARGUMENTS'''
'POSITIONAL ARGUMENT'
'DEFAULT ARGUMENT'
'VARIABLE LENGTH POSITIONAL ARGUMENT''IMPORTANT'
'KEYWORD POSITIONAL ARGUMENT'
'DEFAULT KEYWORD ARGUMENT'
'VARIABLE LENGTH KEYWORD ARGUMENT''IMPORTANT'


'''POSITIONAL ARGUMENT'''

# def add(x,y):
#     print(x)
#     print(y)
# z = add(10,20)


# def name(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# p = int(input("Enter 1st value :"))
# q = int(input("Enter 2nd value :"))
# r = int(input("Enter 3rd value :"))

# name(p,q,r)



# def name(name,age,qualification):
#     print(name)
#     print(age)
#     print(qualification)
# p = (input("Enter 1st value :"))
# q = int(input("Enter 2nd value :"))
# r = (input("Enter 3rd value :"))

# name(p,q,r)


'''DEFAULT ARGUMENT'''


# def name(name = "Guest",age = None,qualification = None):
#     print(name)
#     print(age)
#     print(qualification)
# p = (input("Enter 1st value :"))
# q = int(input("Enter 2nd value :"))
# r = (input("Enter 3rd value :"))

# name()

'''VARIABLE LENGTH ARGUMENT OR VARIABLE LENGTH POSITIONAL ARGUMENT''' 'IMPORTANT'

# def add(*n):
#     print(n)
#     print(type(n))

# add()
# add(2)
# add(2,3,4,5,6,7,8,9,10)



# def add(*n):
#     sum = 0
#     for i in n:
#         sum+=i
#     print(sum)
# add()
# add(1)
# add(1,2,3,4,5,6,7,8,9,10)




# def add(*n):
#     print(n)
#     print(type(n))

# add()
# add(2)
# add(2,3,4,5,6,7,8,9,10)



# def add(n):
#     print(n)
#     print(type(n))
# n = int(input("Enter how many values you want to add :"))

# l = []

# for i in range(n):
#     value = float(input("Enter an Number :"))
#     l.append(value)

# add(l)



# x = 10
# print(type(x))




# def add(*n):
#     sum = 0
#     for i in n:
#         for j in i:
#             sum = sum+j
#     print(sum)

# n = int(input("Enter how many values you want to add :"))

# l = []

# for _ in range(n):
#     value = float(input("Enter an Number :"))
#     l.append(value)
# add(l)

'NESTED FORM'

# def add(n):
#     sum = 0
#     for i in n:
#      sum+=i
#     print(sum)

# n = int(input("Enter how many values you want to add :"))

# l = []

# for _ in range(n):
#     value = float(input("Enter an Number :"))
#     l.append(value)
# add(l)


'''KEYWORD  POSITIONAL ARGUMENT'''

# def add(x,y):
#     print(x+y)

# p = int(input("Enter Number :"))
# q = int(input("Enter Number :"))

# add(x=p,y=q)
# add(y=p,x=q)



'''DEFAULT KEYWORD ARGUMENT'''

# def add(x=0,y=0):
#     print(x+y)

# p = int(input("Enter Number :"))
# q = int(input("Enter Number :"))

# add()
# add(x=p)
# add(y=q)
# add(y=p,x=q)

'''VARIABLE LENGTH KEYWORD ARGUMENT''' 'IMPORTANT'

# def name(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# name()
# name(x=10)
# name(x=10,y=20,z=30,p=40,q=50)



# def name(**n):
#     for k,v in n.items():
#         print(k,'=',v)

# name(x=10,y=20,z=30,p=40,q=50)



# def name(**n):
#     print(n)
#     print(type(n))

# d = {'x' : 10,'y' : 20,'z' : 30}

# name(x=d)
# name(**d)

# def name(**n):
#     for k,v in n.items():
#         for j,l in v.items():
#             print(j,'=',l)
# d = {'x':10,'y':20,'z':30}
# name(x=d)



# def leapyear(year):
#     if year%4==0 and year%100!=0 or year%400==0:
#      print(f'Year {year} is leap_year')
#     else:
#        print(f'Year {year} is not a leap_year')
    

'FIBONACCI SERIES'

# n = int(input("Enter Number :"))
# a,b = 0,1

# for _ in range(n):
#     print(a,end=' ')
#     a,b=b,a+b

'OR THROUGH FUNCTION'

# def fib(n):
#  a,b = 0,1

#  for _ in range(n):
#     print(a,end=' ')
#     a,b=b,a+b

# fib()

'OR'

# def fibo():
#     n = int(input("Enter Number :"))

#     a,b = 0,1

#     for _ in range(n):
#         print(a,end=',')
#         temp = a
#         a = b
#         b = temp + b

# fibo()

'''TO FIND LENGTH'''

# s = [1,2,3,'viras',17]

# len = 0

# for _ in s:
#     len = len+1
# print(f'The length of given {s} is {len}')


'OR THROUGH FUNCTION'


# def length():

#    s = [1,2,3,'viras',17]

#    len = 0
#    for _ in s:
#     len = len+1
#    print(f'The length of given {s} is {len}')
# length()




'''TO FIND MAXIMUM'''

# l = [10,30,20,40,60]

# max = l[0]

# for i in l:
#     if max<i:
#         max = i
# print(f'maximum value of given {l} is {max}')

'OR THROUGH FUNCTION'

# def length():
    
#    l = (20,40,60,10)
#    max = l[0]

#    for i in l:
#       if max < i:
#          max = i
#    print(f'the Maximum of Given {l} is {max}')

# length()


'''TO FIND MINIMUM'''

# l = [10,30,20,40,60]

# min = l[0]

# for i in l:
#     if min>i:
#         min = i
# print(f'maximum value of given {l} is {min}')

'OR THROUGH FUNCTION'

# def length():
    
#    l = (20,40,60,10)
#    min = l[0]

#    for i in l:
#       if min > i:
#          min = i
#    print(f'the Minimum of Given {l} is {min}')

# length()


'''TO FIND SUM'''

# l = [10,30,20,40,60]

# sum = 0
# for i in l:
#     sum+=i
# print(f'sum is {sum}')

'OR THROUGH FUNCTION'

# def length():
    
#    l = (20,40,60,10)
#    sum = 0

#    for i in l:
#       sum+=i
#    print(f'the sum of Given {l} is {sum}')

# length()