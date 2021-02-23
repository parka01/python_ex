#사용자로부터 두 개의 숫자를 입력받아 두 숫자 사이(두 숫자 포함)의
#소수를 출력하는 프로그램을 작성하시오. 두 개의 숫자를 매개변수로
#받아서 두 숫자 사이의 소수를 출력하고, 소수의 개수를 반환하는
# 부분을 findPrime(x,y)함수로 작성하시오.
num=int(input('첫 번째 숫자(작은 수) 입력: '))
num2=int(input('두 번째 숫자(큰 수) 입력'))
for i in range(num,num2+1):
    count = 0
    
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count <= 2:
        print(i)