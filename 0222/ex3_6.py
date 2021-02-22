num=input('좋아하는 월은? ')
month=int(input('현재 월 입력(정수): '))
if((month<1)or(month>12)):
    print("잘못된 입력")

elif((month>=3))and(month<=5)):
    print("봄")
elif((month>=6))and(month<=8)):
    print("여름")
elif((month>=9))and(month<=11)):
    print("가을")
else:
    print("겨울")