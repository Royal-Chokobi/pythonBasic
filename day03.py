print("a = ", 10)
print("a = %d b = %d" %(10, 20))
print("a = {} b = {} c = {}" .format(10,20,30))

'''
    위 3가지 중 python3에서 .format()을 가장 많이 사용함.
'''

print("hello")
print("world")

print("="*50)

print("hello", end="-엔터대신해서 사용됨-")
print("world")

print("hello", "world", sep="-중간에!!! 들어가랏!-", end="끝~\n")

print("="*50)

s = "0123456789"

'''
    s = '0123456789'
    ->  [012345678910]
    -> stringValue[0] = 'H'
    -> TypeError 발생! (immutable 하기 때문)
'''

for i in range(0, len(s)):
    print(s[i])

print("="*50)
print(s[0])
print(s[0:5])
print(s[-7:-2])
print(s[2:-2])
print(s[:])
print(s[::3])
print(s[:10])
print(s[1:10:3])
print(s[10:1:-3])
print(s[:1:-3])

str = 'hello world'
# str = str.replace('h','H')
print(str)

print("하"*10)

if 'hello' in str:
    print(True)
else:
    print(False)

if 'world' not in str:
    print(True)
else:
    print(False)

print(str.upper())
print(str.lower())
print(str.isupper())
print(str.islower())
print(str.title())
print(str.istitle())
print(str.capitalize())

