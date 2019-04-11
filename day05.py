'''
리스트
'''

score = [10,20,30,40,50]
print(score)
print(len(score))
print(score[:5])
print(score[:5:2])
score1 = [1,2,3,4,5]
m = score+score1
print(m)
m.sort()
print(m)
m.reverse()
print(m)

score.append(15)
print(score)
score.insert(2,25)
print(score)

k = score.pop()
print(k)
print(score)
k = score.pop(2)
print(k)
print(score)
score.remove(20)
print(score)
print(score.index(40))
print(score.count(40))

score.clear()
print(score)

arr = [1,6,5,3,7,2,9,8,0]
arr.sort() #오름차순
print(arr)
arr.sort(reverse=True) #내림차순
print(arr)

lt = tuple(arr)
print(lt)
# lt[0] = 10 에러남... 변동 불가.
# tuple 과 list의 차이가 있음!!!!



