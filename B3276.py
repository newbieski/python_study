n = int(input())
sum = n + 1
a = 1
b = n
for i in range(1, n) :
    for j in range(1, n) :
        if i * j >= n and i + j < sum :
            sum = i + j
            a = i
            b = j
print(a, b)

a=1
b=1
n=int(input())
while a*b<n:
    if a>b: b+=1
    else : a+=1
print(a,b)