#1번
t = 'Alice'[2:]
w = 'car epatm'

t += ' '+w[::2]

print(t)

#2번
n = int(input('Enter n : '))
num = list(range(1, n+1))
print("L : {}".format(num))
print("M : {}".format(num[::2]))


#3번
score = [80, 90, 88, 56, 77, 93, 82, 92, 75, 83]
#percent = int(input('Enter percent : '))
score.sort()



print(score[-2]*0.1)


#4번
i = 0
cnt_2 = 0
cnt_3 = 0
while i < 5:
    n = int(input('n 입력 : '))
    if n%2 > 0:
        cnt_3 +=1
    else:
        cnt_2 +=1
    i+=1

if cnt_2 > cnt_3:
    print("짝수가 {}개 더 많이 입력되었습니다.".format(cnt_2 - cnt_3))
else:
    print("홀수가 {}개 더 많이 입력되었습니다.".format(cnt_3 - cnt_2))
