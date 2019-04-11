print('[2번] 10개의 정수를 입력받아서 양의 정수, 0, 음의 정수의 개수를 출력하는 프로그램을 작성하시오. 반드시 while 루프를 이용하여 10개의 정수를 입력받는다.')

num = 1
positive_number = 0
zero_number = 0
negative_number = 0
while num <= 10:
    input_number = int(input('Enter number : '))
    if input_number > 0: positive_number += 1
    elif input_number < 0: negative_number += 1
    else: zero_number += 1
    num += 1

print(' positive number : %d \n zero : %d \n negative number : %d' % (positive_number, zero_number, negative_number))
