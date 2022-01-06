dict1 = dict()
print(dict1, type(dict1))
print('----------------------------------')

dict2 = {}
print(dict2, type(dict2))
print('----------------------------------')

dict3 = {
    'v1' : 100,
    'v2' : 11.11
}
print(dict3, type(dict3))

a1 = dict3['v1']
a2 = dict3['v2']
print(a1, a2)
print('----------------------------------')
dict3['v3'] = True
print(dict3, type(dict['v3']))
print('----------------------------------')

dict3['v3'] = "abc"
a = dict3['v3']
print(dict3, type(dict['v3']), type(a))

del dict3['v3']
print(dict3)
print('----------------------------------')
#a1 = dict3['v100']
#print(a1)
# None이 반환
a1 = dict3.get('v100')
print(a1)
print('----------------------------------')

print(dict3)
a1 = dict3.items()
print(a1, list(a1))
print(type(dict3.items()))
for a2 in dict3.items() :
    print("a2 ", a2, type(a2))
    #print(f'{a2} : {a3}')

a10 = dict3.keys()
print(a10)

a11 = dict3.values()
print(a11)