n = int(input())
n1 = n
if n % 2 == 0 : n1 = n - 1
ans = 0

def calc(k) :
    cnt = 0
    while k <= n :
        cnt += 1
        k *= 2
        k += 2
    return cnt

def lower(k) :
    l, r = 1, n1
    res = r
    while l <= r :
        mid = (l + r) // 2
        if mid % 2 == 0 : mid -= 1
        tmp = calc(mid)
        if tmp > k :
            l = mid + 2
        elif tmp < k :
            r = mid - 2
        else :
            if mid < res : res = mid
            r = mid - 2
    return res

def upper(k) :
    l, r = 1, n1
    res = r + 2
    while l <= r :
        mid = (l + r) // 2
        if mid % 2 == 0 : mid -= 1
        tmp = calc(mid)
        if tmp >= k :
            l = mid + 2
        else :
            if mid < res : res = mid
            r = mid - 2
    return res

if n >= 2 : ans += (calc(2) + 1) // 2
mx = calc(1)
for i in range(mx, 0, -1) :
    l, u = lower(i), upper(i)
    ans += (i + 1) // 2 * ((u - l) // 2)
print(ans)