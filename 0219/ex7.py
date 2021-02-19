num=int(input('소수 검증 숫자 입력: '))
for i in range(2,int(num/2))
    if num%i==0:
        print('소수가 아니다.')
        break
else:
    print('소수이다.')
print('소수 판별 프로그램을 이용해주셔서 감사합니다.')