from urllib.parse import parse_qs
my_values = parse_qs('kr=한국&red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))
# {'kr': ['한국'], 'red': ['5'], 'blue': ['0'], 'green': ['']}

print('kr:     ', my_values.get('kr'))
print('red:     ', my_values.get('red'))
print('blue:     ', my_values.get('blue'))
print('green:     ', my_values.get('green'))
"""
kr:      ['한국']
red:      ['5']
blue:      ['0']
green:      ['']
"""

''' 위의 get을 가져오는 방법에서 빈값을 모두 0으로 처리 / 좋은 방법은 아님 '''
kr = my_values.get('kr', [''])[0] or 0
red = my_values.get('red', [''])[0] or 0
blue = my_values.get('blue', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0

print('kr:     %r' % kr)
print('red:    %r' % red)
print('blue:   %r' % blue)
print('green:  %r' % green)

"""
kr:     '한국'
red:    '5'
blue:   '0'
green:  0
"""

"""
int로 파싱을 위해 
> red = int(my_values.get('red', [''])[0] or 0)
이렇게 사용하는건.. 좋지 못하다. 가독성이 많이 많이 떨어짐!
"""

red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0 # 삼항 표현식
print(red)
# 5

# red = int(red[0]) if red[0] else 0 를 if문으로 정의하면 아래와 같다.
# 하지만 오히려 풀어쓰면 더 복잡하게 느껴짐.
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0
print('green:  %r' % green)

# 그러므로 반복적으로 자주 사용하는 경우 헬퍼 함수를 만들어 사용하자!
# 코드가 복잡해지면 최대한 빨리 해당 표현식을 작은 조각으로 분할도 고려해야함!
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    print('get_first_int : %r' % found)
    return found

green = get_first_int(my_values, 'grean')
red = get_first_int(my_values, 'red')
'''
get_first_int : 1
get_first_int : 5
'''