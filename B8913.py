import sys
import collections
input = sys.stdin.readline

cache = collections.defaultdict(int)

def compress(str, k) :
    l = len(str)
    if k > 0 and str[k - 1] == str[k] : return "c"
    r = k
    while r < l and str[k] == str[r] : r += 1
    if r - k == 1 : return "c"
    return str[:k] + str[r:]

def dp(str) :
    if len(str) == 0 : return 1
    if len(str) == 1 : return 2
    if cache[str] != 0 : return cache[str]
    res = 0
    for i in range(len(str)) :
        s = compress(str, i)
        if s == "c" : continue
        res |= dp(s)
    cache[str] = res
    #print("dp", str, res)
    return res

n = int(input())
for _ in range(n) :
    s = input().strip()
    print(dp(s) & 1)