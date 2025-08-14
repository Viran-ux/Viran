
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


