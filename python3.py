n = int(input("Enter an Number :"))

for i in range(1,n+1):
    j = 'A'
    for _ in range(1,n+1):
        print(j,end=' ')
        j = chr(ord(j)+1)
    print()