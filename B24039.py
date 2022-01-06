def isprime(x) :
    i = 2
    while i * i <= x :
        if x % i == 0 : return False
        i += 1
    return True
p = []
for i in range(2, 120) :
    if isprime(i) :
        p.append(i)
    i += 1

n = int(input())
for i in range(len(p)) :
    if n < p[i] * p[i + 1] :
        print(p[i] * p[i + 1])
        break
