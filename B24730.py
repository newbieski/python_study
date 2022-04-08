n = int(input())
f = [*map(int, input().split())]
MOD = 10**9+7

def fx(x) :
    res = 0
    p = 1
    for i in range(n + 1) :
        res += f[i] * p
        p *= x
    return res % MOD

arr = [fx(i) for i in range(n + 1)]
ans = []
for i in range(n + 1) :
    ans.append(arr[0] % MOD)
    for j in range(n - i) :
        arr[j] = (MOD + arr[j + 1] - arr[j])
s = ",".join([str(i) for i in ans])
print(f'GGG<{s}>')