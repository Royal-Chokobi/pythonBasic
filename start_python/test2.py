#3번
score = [80, 90, 88, 56, 77, 93, 82, 92, 75, 83]
percent = int(input('Enter percent : '))
score.sort(reverse=True)
percent = int(percent*0.1)

print(score[:percent])