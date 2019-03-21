import keyword

def changeNumber(x, y) :
    print('교환전  : ', x, y)
    x, y = y, x
    print('교환후 : ', x, y)

print('hello')
print('기초수업')

score1 = 100
score2 = 200
score3 = 300
total = score1+score2+score3
print(score1, score2, score3)

print(total)

x = 10
y = 2.5

print(type(x))
print(type(y))

print(keyword.kwlist)

s1 = 90
s2 = 90
s3 = 90
total_s = s1+s2+s3
print(total_s)


a = 10
b = 20
print('a와 b를 출력 : ', a, b)

a1 = a
a = b
b = a1
'''
    파이썬은 자료 교환이 
        a, b = b, a
    가 적용이 됨.
'''
print('a와 b를 교환해서 출력 : ', a, b)

changeNumber(10, 20)

print('==============================수치 자료형과 계산하기==========================================')

def numberCalculation(x, y):
    print('더하기 : ',x+y)
    print('빼기 : ',x-y)
    print('곱하기 : ', x*y)
    print('제곱 : ', x**y)
    x,y = y,x
    print('x,y = y,x')
    print('나누기 : ',x/y)
    print('몫구하기 : ', x//y)
    print('나머지 : ',x%y)

numberCalculation(2,11)


print('=================================문제~ ==================================================')

x = 1479

a = (x//1000)
b = (x//100)%10
c = ((x//10)%100)%10
d = x%10


print(a)
print(b)
print(c)
print(d)

print('=========================')

n= 2500

h = (n//(60*60))
m = (n - (h*(60**2)))//60
s = n - ((h*(60**2)) + (m*60))

print(h)
print(m)
print(s)


print(0.2+0.1)