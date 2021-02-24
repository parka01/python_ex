'''a=int(input('숫자를 입력하시오: '))
b=int(input('또 다른 숫자를 입력하시오: '))

def plusNumber(a,b):
    total=a+b
    return total
total=plusNumber(a,b)
print('두 숫자의 합: ',total)'''


#----------모범답안----------
def hap(a,b):
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    print('두 수 사이의 합: ',sum)
#메인프로그램
num1=int(input('첫 번째 숫자: '))
num2=int(input('두 번째 숫자: '))
hap(num1,num2)
#첫번째 숫자가 큰 경우는 안나오기때문에 range에서 안먹힌다
#그래서 뒤바꿔주는 것을 넣으면 된다.