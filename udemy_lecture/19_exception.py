try :
    a1 = 10 // 0
    print(a1)
except :
    print('exception occured')

print("????????")

print('-'*40)

try :
    a1 = 10 // 0
    print(a1)
    #list1 = [10, 20, 30]
    #print(list1[10])
    # a1 = 10 // 2
    # print(a1)
except ZeroDivisionError :
    print('exception occured : divided by zero')
except IndexError :
    print("exception : list")
except Exception :
    print('exception : etc')
else :
    print('exception is not occured')
finally :
    print('all is done')

print('end of process')

