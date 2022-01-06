n=int(input())
l,r=1,n
while l <= r :    
    mid = (l + r) // 2
    t = mid ** 2
    if t == n :
        print(mid)
        break
    elif t < n : l = mid + 1
    else : r = mid - 1

import math
print(math.isqrt(int(input())))