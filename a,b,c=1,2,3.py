x=[]
s=int(input())
a=list(map(int,input().split()))

n=int(input())
b=list(map(int,input().split()))

for i2 in range(len(b)):
    if b[i2] in a:
        x.append(1)
    else :
        x.append(0)

print(*x)