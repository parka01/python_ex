'''num=int(input('소수 검증 숫자 입력: '))
def prime(num):
    for i in range(2,int(num/2)):
        if num%i==0:
            print('소수가 아니다.')
            break
    else:
        print('소수이다.')

    return'''

#----------모범답안----------
def prime(num):
    for i in range(2,num):
        if num%i==0:
            print('소수가 아니다')
            break
        else:
            print('소수이다.')

#메인프로그램
num=int(input('소수 검증 숫자 입력: '))
prime(num)

#----------모범답안----------
def prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
        if flag==0:
            print(num,'은 소수이다.')
        else:
            print(num,'은 소수가아니다.')
#메인프로그램
num=int(input('소수 검증 숫자 입력: '))
prime(num)