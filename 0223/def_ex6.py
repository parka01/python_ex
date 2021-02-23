#사용자로부터 두 개의 숫자를 입력받아 두 숫자 사이(두 숫자 포함)의
#소수를 출력하는 프로그램을 작성하시오. 두 개의 숫자를 매개변수로
#받아서 두 숫자 사이의 소수를 출력하고, 소수의 개수를 반환하는
# 부분을 findPrime(x,y)함수로 작성하시오.
def findPrime(x,y):
    print(x,'부터',y,'사이의 소수: ',end=' ')
    cnt=0
    for i in range(x,y+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=' ')
            cnt=cnt+1
    else:
        print('')
    return cnt

num1=int(input('첫번째 숫자: '))
num2=int(input('첫번째 숫자: '))

cnt=findPrime(num1,num2) #실매개변수는 num1,num2
print('소수는 모두 ',cnt,'개 입니다.')