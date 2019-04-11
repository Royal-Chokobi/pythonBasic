print('[1번] 환율을 입력받아서 원화를 달러로, 또는 달러를 원화로 바꾸어 출력하는 문제이다. 출력 결과를 보고 코드를 작성하시오.')

now_rate = int(input('Enter currency rate : '))
if now_rate > 0:
    print('Today`s rate is %.2f won for 1$' % now_rate)
    input_type = int(input('If you want to exchange from Won to Dollar, input 1 \n'
                           'If you want to exchange from Dollar to Won, input 2 : '))
    if input_type == 1:
        exchange_money = int(input('Exchange from Won to Dollar : \n'
                                   'How much do you want to exchange (in Won)? '))
        print('you get %.2f dollars for %.2f won' % (exchange_money/now_rate, exchange_money))
    elif input_type == 2:
        exchange_money = int(input('Exchange from Dollar to Won : \n'
                                   'How much do you want to exchange (in Dollar)? '))
        print('you get %.2f won for %.2f dollars' % ((exchange_money*now_rate), exchange_money))

    else:
        print('Wrong input! You should input 1 or 2!!')
else:
    print('error : 숫자는 0보다 커야합나다.')
