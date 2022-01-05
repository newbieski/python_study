str1 = 'hello'
str2 = "hello"

print(str1, type(str1))
print(str2, type(str2))

str1 = "my name is 'blah blah'"
str2 = 'my name is "bbb"'
print(str1, str2)

str3 = ''' "name" '30' '''
str4 = """ "name" '30' """
print(str3, str4)

str5 = '''abc
def
ghi'''
print(str5)

str6 = """abdefg
hijkl"""
print(str6)

print('-----------------------------------------------')

a1 = 'haha'
a2 = 30
a3 = 180

str1 = 'name is ' + a1 + ' and age is ' + str(a2) + '. ' + 'height ' + str(a3) + ' cm'
str2 = 'name %s age %d name %s height %d' %(a1, a2, a1, a3)
str3 = 'name {0}, age {1}, name {0}, height {2}'.format(a1, a2, a3)
str4 = f'name {a1} age {a2}, name {a1}, height {a3}'
print(str1)
print(str2)
print(str3)
print(str4)

print('-----------------------------------------------')
str1 = 'abcdefg'
print(str1[0])
print(str1[1])
print(str1[-1])
print(str1[-2])

# 2 ~ 5 - 1
print(str1[2:5])
print(str1[:5])
print(str1[2:])

print('-----------------------------------------------')
str1 = 'str1' + 'str2'
print(str1)

# str2 = 'str1' + 100

str3 = 'str' * 3
print(str3)
print('-----------------------------------------------')
str1 = 'abcdefg'
str2 = '가나다라마바사'
a1 = len(str1)
a2 = len(str2)
print(a1, a2)

print('-----------------------------------------------')
str1 = 'hello world'
str2 = str1.capitalize()
print(str2)

print('-----------------------------------------------')
str1 = 'python'
str2 = str1.center(40, "_")
print(str2.ljust(50, "*").rjust(60, "!"))

str1 = 'abcd abcd abcd aaaa'
a1 = str1.count('abcd')
print(a1)
a2 = str1.count("a")
print(a2)
# 앞에서부터 10글자를 제외하고 a가 몇개
a3 = str1.count('a', 10)
print(a3)

# 앞에서부터 10글자 제외, 인덱스 15부터 제외 (--> 10 ~ 15- 1 같음)
a4 = str1.count('a', 10, 15)
print(a4)

a1 = str1.startswith('abc')
a2 = str1.startswith('zzz')
print(a1, a2)

a3 = str1.endswith('efg')
a4 = str1.endswith('zzz')
print(a3, a4)
print('-----------------------------------------------')

str1 = 'abcdefg'
a1 = str1.find('cde')
a2 = str1.index('cde')
print(a1, a2)

a3 = str1.find('zzz')
#a4 = str1.index('zzz')
#print(a3, a4)

print('-----------------------------------------------')
str1 = 'abcd1234'
a1 = str1.isalnum()
print(a1)

str2 = '123456'
a2 = str2.isdigit()
print(a2, str2.isnumeric())

str3 = 'abcdefg'
a3 = str3.isalpha()
print(a3)

str4 = 'abcdeABCDEFG'
a4 = str4.islower()
print(a4)

str5 = 'ABCD'
a5 = str5.isupper()
print(a5)

# 주어진 구분자로 튜플이나 리스트가 가지고 있는 값을 합쳐서 문자열로 생성한다
str1 = '!@-'
str2 = ['aaa', 'bbb', 'ccc']
#str4 = ['aaa', 100, 11.11]
str3 = str1.join(str2)
print(str3)

print('-----------------------------------------------')

str1 = 'ABcdEF'
str2 = str1.lower()
str3 = str1.upper()
print(str2, str3)

print('-----------------------------------------------')
str1 = 'abcdefg'
str2 = str1.replace('cde', 'zzzzzzzz')
print(str2)

print('-----------------------------------------------')
str1 = 'ab cd_ef gh'
a1 = str1.split()
print(a1, type(a1))
a2 = str1.split("_")
print(a2)