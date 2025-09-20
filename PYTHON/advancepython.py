'''ADVANCE PYTHON STARTS FROM HIGHER ORDER FUNCTION'''


'HIGHER ORDER FUNCTION'

'VERBOSE CONDITION' 'long function definition with if/else'

# def evn(x):
#     if x%2==0:
#         return x
#     else:
#         return None
    
# l = [1,2,3,4,5]

# print(list(filter(evn,l)))

'CONCISE CONDITION' 'short one-liner, often with lambda'

# l = [1,2,3,4,5]

# print(list(filter(lambda x:x%2==0,l)))


'MAP'


'1,SQUARING'

# l = [1,2,3,4,5]

# def square(n):
#     return n**2
# result = map(square,l)
# print(list(result))

'2,ADDING'

# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,10]

# def add(x,y):
#     return x+y
# result = map(add,l1,l2)
# print(list(result))

'FILTER'

# l = [1,2,3,4,5,6]

# def even(x):
#     return x%2==0

# print(list(filter(even,l)))



# l = [-2,-1,0,1,2,3,-5,-6]

# def posi(x):
#     return x>0

# print(tuple(filter(posi,l)))


'REDUCE'

'THROUGH //FROM FUNCTOOLS IMPORT REDUCE' 

# from  functools import reduce
# l = [1,2,3,4,5]

# def sum(x,y):
#     return x+y
# x = reduce(sum,l,0)
# print(x)

'IMPORT FUNCTOOLS AND THEN FUNCTOOLS.REDUCE WHILE ASSIGNING'

'MAXIMUM' 'VERBOSE CONDTION NOT USED LAMBDA'

# import functools

# l = [10,30,20,5,40,60]

# def max_digit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
    
# x = functools.reduce(max_digit,l)

# print(x)

'MINIMUM' 'VERBOSE CONDTION NOT USED LAMBDA'

# import functools

# l = [10,30,20,5,40,60]

# def min_digit(x,y):
#     if x<y:
#         return x
#     else:
#         return y
    
# x = functools.reduce(min_digit,l)

# print(x)

'LAMBDA FUNCTION'

# x = lambda x,y:x+y

# print(x(4,5))

'MAX THROUGH LAMBDA' 'CONCISE CONDITION USED LAMBDA'

# from functools import reduce

# l = [1,3,5,9,7,4]

# x = reduce(lambda x,y:x if x>y else y,l)

# print(x)

'GREAT. THAN 2 THROUGH LAMBDA' 'CONCISE CONDITION USED LAMBDA'


# l = [1,3,5,3,7,4]

# x = list(filter(lambda x:x if x>2 else None,l))

# print(x)


'MAP,FILTER,REDUCE COMBINED' 


# from functools import reduce

# l = [1,2,3,4,5,6]

# result = reduce(
#     lambda x, y: x + y,                          # reduce → sum them up
#     map(lambda x: x**2,                          # map → square each
#         filter(lambda x: x % 2 == 0, l))      # filter → keep evens
# )

# print(result) # 56  (2² + 4² + 6² = 4 + 16 + 36)



'DECORATOR''=''a decorator is a special function that lets you modify the behavior of another function (or class) without changing its code.'



# def outer_fun(func):  # accepts a function, not "name"
#     def inner_fun(p, q):
#         p = p + 10
#         q = q + 20
#         res = func(p, q)  # call the passed-in function
#         return res
#     return inner_fun   # return the wrapper

# def add(x, y):
#     return x + y

# a = outer_fun(add)   # wrap add with outer_fun
# b = a(5, 10)         # call the new function
# print(b)


'@ Decorator used in below'

# def outer(func):  # outer acts as a decorator
#     def inner(p, q):
#         p = p + 10
#         q = q + 20
#         res = func(p, q)  # use the original function
#         return res
#     return inner  # return the wrapped function, not call it

# @outer
# def add(x, y):
#     return x + y

# r = add(5, 10)
# print(r)



'GENERATOR'

# def new (n):
#     for i in range(1,n+1):
#         yield i

# res = new(10)
# print(next(res))
# print("Hello")
# print("Hi")
# print(next(res))
# print(next(res))
# print(next(res))




# def new (n):
#     for i in range(1,n+1):
#         yield i

# res = new(10)
# print(next(res))
# def even_odd():
#     n = 5
#     if n%2==0:
#         print("EVEN")
#     else:
#         print("ODD")
# even_odd()
# print("Hello")
# print("Hi")
# print(next(res))
# print(next(res))
# print(next(res))

'differnce in return and yield'

'''1. return
Used inside a normal function.

Ends the function immediately.

Sends back a single final value to the caller.

Once return executes, the function cannot resume.'''


'''2. yield
Used inside a generator function.
Doesnt end the function permanently. Instead:
It pauses execution.
Remembers the functions state.
Can resume from where it left off when called again.
Produces a sequence of values, one at a time.
More memory efficient than return when working with large datasets.'''



'OOPS' 


'MAGIC METHODS'

# class student:
#     "details for student"
#     pass

# print(dir(student))

# print(student.__doc__)
# print(student.__dict__)
# print(student.__module__)

'''ID WILL BE SAME '''

# class student:
#     "Details for student"
#     pass

# print(id(student))
# obj1 = student
# obj2 = student
# obj3 = student

# print(id(obj1),id(obj2),id(obj3))

'EXTERNAL CONSTRUCTOR CALLED AND AFTER THAT USED INTERNAL CONSTRUCTOR'

# class student:
#     def __init__(self):
#         print("Constructor called")
    
# obj = student()

# obj.__init__()

'THE CONSTRUCTOR IS CALLED BY DEFAULT AND FIRST PARAMETER IS SELF SO SELF HOLDS THE CURRENT CLASS CURRENT OBJECT ADDRESS HENCE ITS SAME'

# class student:
#     school = 'MVM'
    

# obj1 = student
# print(obj1.school)

# obj2 = student
# print(obj2.school)
# print(id(obj1),id(obj2),id(student))

'THE SELF HOLDS THE SAME ADDRESS AS THE CURRENT CLASS WHICH CONTAIN THE OBJECT'

# class student:
#     def __inti__(self):
#         print(id(self))

# obj1 = student
# print(id(student))

'A CLASS WHICH CONTAINS OBJECTS '

# class student:
#     def __init__(self,name,grade):
#         self.n = name
#         self.g = grade

# obj1 = student('Vira','B-Tech')
# print(obj1.n,obj1.g)
# obj2 = student('doha','Qatar')
# print(obj2.n,obj2.g)


'USE OF GLOBAL'

# def new():
#     global x
#     x = 10
#     print(x)

# new()
# print(x)

'TYPES OF VARIABLES'

'INSTANCE = An instance variable is a variable which is declared in a class but outside of constructors, methods, or blocks. '
'STATIC/CLASS = This means it can be called directly on the class itself, without the need to create an instance of the class. '
'LOCAL = Local variables are created inside a function and exist only during its execution. They cannot be accessed from outside the function.'