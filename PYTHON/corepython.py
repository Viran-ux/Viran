'''CORE PYTHON STARTS FROM HIGHER ORDER FUNCTION'''


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