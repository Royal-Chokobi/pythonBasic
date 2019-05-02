import random as ran

num = ran.randint(1,10)
print(num)

m = [ran.randrange(20) for i in range(10)]
print(m)

n = ran.sample(range(20),10)
print(n)