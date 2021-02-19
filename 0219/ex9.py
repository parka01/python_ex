num1=input('1 번째 성적 입력: ')
num2=input('2 번째 성적 입력: ')
num3=input('3 번째 성적 입력: ')
num4=input('4 번째 성적 입력: ')
num5=input('5 번째 성적 입력: ')

if num1>0 or num1<100:
    print('유효한 성적이 아닙니다.')

num2=input(2 번째 성적 입력: )
if num1>0 or num1<100:
    print('유효한 성적이 아닙니다.')
else:
    print(1 번째 성적:)
num3=input(3 번째 성적 입력: )
if num1>0 or num1<100:
    print('유효한 성적이 아닙니다.')
else:
    print(1 번째 성적:)
print(3 번째 성적:)
num4=input(4 번째 성적 입력: )
print(4 번째 성적:)
num5=input(5 번째 성적 입력: )
else:
    print(5 번째 성적:)
print(5 번째 성적:)
print('총점: ')
print('평균: ')
#----------모범답안----------
sub=1
total=0

while sub<=5:
    score=int(input(str(sub)+'번째 점수 입력: '))
    if (score>=0 and score<=100):
    total=total+score
    print(sub, "번째 성적:",score)
    sub=sub+1
    else:
        print('유효한 성적이 아닙니다.')

print('총점: ', total)
print('평균: ', total/5)