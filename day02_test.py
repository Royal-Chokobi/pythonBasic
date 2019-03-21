'''2일차 문제'''

#문제 1번
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

x1 = (-b+(b**2-(4*a*c))**0.5)/(2*a)
x2 = (-b-(b**2-(4*a*c))**0.5)/(2*a)

print(a,b,c)
print(x1,x2)


#문제 2번
price = int(input('입장료를 입력하세요 : '))
print('원래 입장 금액 : %d \n' 
      "할인된 금액 : %0.1f \n"
      "적립된 금액 : %0.1f " %(price,(price*0.8), (price*0.8)*0.04))