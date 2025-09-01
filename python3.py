
n = int(input("Enter an Number :"))

for i in range(0,n+1):
    print(' '*i+'* '*(n-i))
print('*'*())
for i in range(2,n+1):
    print(' '*(n-i)+'* '*i)