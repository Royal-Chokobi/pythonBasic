a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))
max = 0
if a > b:
    if a > c:
       max = a
    else:
        max = c
elif b > c:
    max = b
else:
    max = c

print(max)


cnt = int(input('enter n : '))
highest = 0
a = 1
while a <= cnt:
  a+=1
  sc = int(input('enter score : '))
  if highest < sc : highest = sc

print(highest)


