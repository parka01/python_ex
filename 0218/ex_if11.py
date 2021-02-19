month=int(input('현재의 월을 입력(숫자): '))
if month==12 or month==1 or month==2:
    print('겨울입니다.')
elif 3<=month<=5:
    print('봄입니다.')
elif 6<=month<=8:
    print('여름입니다.')
elif 9<=month<=11:
    print('가을입니다.')
else:
    print('잘못된 입력입니다.')
#----------------모범답안---------------------
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