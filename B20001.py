cnt = 0
s = input()
while s != "고무오리 디버깅 끝" :
    if (s == "문제") : cnt += 1
    elif (s == "고무오리") :
        if cnt == 0 : cnt += 2
        else : cnt -= 1
    s = input()
    
if cnt > 0 : print("힝구")
else : print("고무오리야 사랑해")