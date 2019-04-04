
math = 95.628
english = 85.42189

print('mathi is %6.2f, english is %10.3f' % (math, english))

if math > english and math >= 0:
    print('큼 = %f' % math)
else:
    print('작음 = %f' % english)

print(math > english)
print(math < english)

score = int(input("점수를 입력하세요 : "))
if score < 70:
    print('성적 %d는 D입니다.' % score)
elif score < 80:
    print('성적 %d는 C입니다.' % score)
elif score < 90:
    print('성적 %d는 B입니다.' % score)
else:
    print('성적 %d는 A입니다.' % score)
    print('축하합니다!!!')

print('오!!!' if score >= 90 else '화이팅!!!')

st_point = 1
while st_point <= 10:
    print("%d hello world" % st_point)
    st_point += 1

number = int(input('최종 합을 할 숫자를 입력 : '))
start_num = 1
sum = 0
while start_num <= number:
    sum += start_num
    start_num += 1
print(sum)


cnt = int(input('enter n : '))
nn = 0
sc=[]
total = 0
while nn < cnt:
  sc.append(input('score : '))
  total += int(sc[nn])
  nn+=1
  if nn == cnt :
      total = total/len(sc)

print(total)