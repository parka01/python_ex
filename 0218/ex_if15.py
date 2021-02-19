num1=int(input('첫 번째 숫자 입력: '))
function=str(input('연산자 + - * /중에서 고르시오!'))
num2=int(input('두 번째 숫자 입력: '))
if function=='+':
    print('수식결과',num1,'+',num2,'=',num1+num2)
elif function=='-':
    print('수식결과',num1,'-',num2,'=',num1-num2)
elif function=='*':
    print('수식결과',num1,'*',num2,'=',num1*num2)
elif function=='/':
    print('수식결과',num1,'/',num2,'=',num1/num2)
else:
    print('해당되는 연산자가 없습니다')
#----------------모범답안---------------------