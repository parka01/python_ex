"""사용자로부터 정수를 입력 받아 정수의 자릿수의 합을
계산하는 프로그램을 작성 하시오. 1234를 입력하였다면 1+2+3+4를 게산
하면 된다."""
num=input('정수를 입력하시오: ')
num2=sorted(num)
num2=map(int,num2)
num2=list(map(int,num2))
print(num2)
sum_result=sum(num2)
print(sum_result)
