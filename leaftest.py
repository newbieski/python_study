def leaf1(year) :
    return (year % 400 == 0) or (year % 100 == 1 and year % 4 == 0)

def leaf2(year) :
    if year % 4 == 0 :
        if year % 100 == 0 : 
            if year % 400 == 0 : return True
            else : return False
        else : return True
    else : return False

for i in range(1900, 10**5 + 1) :
    if leaf1(i) != leaf2(i) :
        print(i)
        print(leaf1(i), leaf2(i))