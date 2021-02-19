num=int(input('배수 숫자 입력: '))
i=0
hap=0
while i<=100:
    i=i+1
    if(i%num)!=0:
        continue #입력된 수의 배수가 아니면 반복문의 처음으로 이동
    #나의 접근방식: 배수값이 *num일때 계속
    hap=hap+1#입력된 수의 배수만 합계에 더함
print('1부터 100까지 {}의 배수의 합은: {}'.format(num,hap))