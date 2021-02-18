score1=int(input('첫 번째 과목의 점수 입력: '))
score2=int(input('두 번째 과목의 점수 입력: '))
sum=score1+score2
if sum>=150:
    if sum>=160:
        if score1>=75 and score2>=75 and sum>=180:
            print('최우수 학생')
        else:
            print('우수학생')
    else:
        print('보통학생')
else:
    print('분발합시다')
#----------------모범답안---------------------
score1=int(input('첫번째 과목점수: '))
score2=int(input('두번째 과목점수: '))
total=score1+score2
if(score1>=75) and (score2>=75):
    if total>=180:
        print('최우수 학생')
    elif total>=160:
        print('우수 학생')
    else:
        print('보통학생')
else:
    print('분발합시다.')