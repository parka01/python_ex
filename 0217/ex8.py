"""패밀리 레스토랑에서 저녁 식사 후 음식 요금이 56000원 나왔다.
10%의 부가세를 포함한다면 지불해야 할 식사 금액이 얼마인지를
구하는 프로그램을 작성 하시오."""
meal=56000
tax=int(meal*0.1)
bill=meal+tax
print(bill)