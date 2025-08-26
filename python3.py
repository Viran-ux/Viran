
'''required n even number'''

# i = 1
# while i<=5:
#     print(2*i)
#     i+=1

# sum = 0
# i = 1
# while i<=5:
#     sum+=i*2
#     if (i<=5-1):
#         print(2*i,end='+')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(sum)

# multi = 1
# i = 1
# while(i<=5):
#     multi = multi*i*2
#     if (i<=5-1):
#         print(2*i,end='*')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(multi)

'''required as user'''

# n = int(input("Enter An Number :"))

# i = 1
# while i<=n:
#     if (i<=n):
#         print(2*i)
#     i+=1

# n = int(input("Enter an Number :"))
# sum = 0
# i = 1
# while i<=n:
#     sum+=i*2
#     if (i<=n-1):
#         print(2*i,end='+')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(sum)

# n = int(input("Enter an Number :"))

# i = 1
# multi = 1
# while i<=n:
#     multi*=i*2
#     if (i<=n-1):
#         print(2*i,end='*')
#     else:
#         print(2*i,end='=')
#     i+=1
# print(multi)

'''required n odd number'''

# i = 1
# while i<=5:
#     print(2*i-1)
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

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print('*'*n)
#     i+=1

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print('*'*i)
#     i+=1

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print(' '*(n-i)+'*'*i)
#     i+=1

# n = int(input("Enter an Number :"))

# i = 1
# while i<=n:
#     print(' '*(n-i)+'* '*i)
#     i+=1


n = int(input("Enter an Number :"))

i = 1
sum = 0
while i<=n:
    sum+=i*2
    if (i<=n-1):
      print(2*i,end='+')
    else:
       print(2*i,end='=')
    i+=1
print(sum)