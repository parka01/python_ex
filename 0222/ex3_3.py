hap=0
cnt=1
while True:
    num=int(input(str(cnt)+'번째 숫자 입력: '))
    if num>0: #0보다 큰 수만 더하기
        hap=hap+num
        cnt=cnt+1
    if cnt>10: #반복문을 종료하는 조건
        break
avg=hap/(cnt-1) #cnt가 11일때 멈췄기 때문
print('전체 합: ',hap)
print('전체 평균: %1.f'%avg) #('전체 평균: ','%1.f'%avg)
