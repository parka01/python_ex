total=0
count=0
while True:
    num=int(input('숫자를 입력: '))
    total=total+num
    count=count+1
    if total>=1000:
        break
print('1000을 넘은 수: ',total,end='')
print(', 평균은 ',total/count)