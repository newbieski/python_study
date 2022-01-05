for i in range(3) :
    a,b = input().split()
    h,m,s = map(int, a.split(":"))
    eh,em,es = map(int, b.split(":"))
    ans = 0
    while True :
        ans += int((h * 10000 + m * 100 + s) % 3 == 0)
        if h == eh and m == em and s == es :
            break
        s += 1
        if s == 60 :
            m, s = m + 1, 0
        if m == 60 :
            h, m = h + 1, 0
        if h == 24 :
            h = 0
    print(ans)