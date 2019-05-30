# 1번

s = ['a','e','i','o','u']
in_str = input("Enter one string : ")
arr = []
k=0
for i in range(len(s)):
    if in_str.find(s[i]) > -1:
        k+=1
        arr.append(s[i])
print(k)
print(arr)

i = 0
count = 0
while i < len(in_str):
    if in_str[i] in 'aeiou': count +=1
    i+=1
print(count)

i=0
count = 0
while i < len(in_str):
    if in_str[i] in s: count +=1
    i+=1
print(count)