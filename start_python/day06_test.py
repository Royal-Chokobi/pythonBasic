L = [90, 80, 77, 92, 95, 75, 88, 82, 91, 79]
print('L : {}'.format(L))
score = int(input('Enter score : '))
L.sort()
print(L[:L.index(score)])

voca = ['a', 'b', 'a', 'c', 'd', 'b']

print(voca)
v_map = {}
i = 0
for i in range(len(voca)):
   v_map[voca[i]] = voca.count(voca[i])

print(v_map)
