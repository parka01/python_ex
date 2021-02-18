score=int(input('점수를 입력하세요: '))
if score>=90:
    print('A학점입니다.')
elif 80>=score<=89:
    print('B학점입니다.')
elif 70>=score<=89:
    print('C학점입니다.')
elif 60>=score<=69:
    print('C학점입니다.')
else score<60:
    print('F학점입니다.')
#----------------모범답안---------------------
score=int(input('점수입력: '))
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=80:
    print('c')
elif score>=80:
    print('D')
else:
    print('F')