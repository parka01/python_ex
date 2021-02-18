"""홍길동의 본봉은 300만원이다. 
이번 달 수당으로 30만원을 받았으며, 
세금으로 총액 20%를 냈다. 
홍길동이 이번 달 월급으로 수령해 간 수령액을 구하는 프로그램을 
작성 하시오."""
salary=int(3000000)
bonus=int(300000)
tax=int((salary+bonus)*0.2)
income=int((salary+bonus-tax))
print(income)
#----------------모범답안---------------------
pay=3000000
extra_pay=300000
tax=(pay+extra_pay)*0.2 #세금
real_pay=(pay+extra_pay)-tax
print("홍길동의 실수령액은 %.0f 만원 입니다."%real_pay)