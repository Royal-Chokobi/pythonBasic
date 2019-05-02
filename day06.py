colorpen= {'red':2, 'blue':3, 'yellow':1}
print(colorpen)


score = {20181234:90, 20181111:80, 20180015:85, 20181007:93}
for k,v in score.items():
    print('학번: {}, 성적: {}'.format(k,v))
D = {}
D[7] = 90
D[5] = 85
D[5] += 2
print(D)
