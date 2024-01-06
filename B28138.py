import sys
n,r=map(int, (input().split()))
n -= r
i = 1
sum = 0
while True :
    if i * i > n :
        break
    if n % i == 0 :        
        if i > r :
            sum += i
        if n // i > r and i != n // i :
            sum += n // i
    i += 1

print(sum)