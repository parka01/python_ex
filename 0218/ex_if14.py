num=int(input('숫자 입력: '))
if num<0:
    print('입력값',num,'은 음수입니다!')
if num>0:
    print('입력값',num,'은 양수입니다!')
if num==0:
    print('입력값',num,'은 0입니다!')
#----------------모범답안---------------------
#단순 if문
num=int(input('숫자입력: '))
if(num<0):
    print('입력값 %d는(은) 음수'%num) #%d는 정수형 변수 실수형은 %f
if(num==0):
    print('입력값 %d는(은) 0'%num)
if(num>0):
    print('입력값 %d는(은) 양수'%num)
#----------------모범답안---------------------
#이중if문
num=int(input('숫자 입력: '))
if(num<0):
    print('입력값 %d는(은) 양수'%num)
elif(num==0):
    print('입력값 %d는(은) 0'%num)
else:
    print('입력값 %d는(은) 양수'%num)