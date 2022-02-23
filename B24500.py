n = int(input())
a, b = 0, 0
while (1<<b) <= n :
    if (n & (1<<b)) == 0 : a += (1<<b)
    b += 1
if a : print(f'2\n{a}\n{n}')
else : print(f'1\n{n}')