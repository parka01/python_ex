hap=0
cnt=1
while cnt<11:
    num=int(input(str(cnt)+'번째 숫자 입력: '))
    cnt=cnt+1
    if cnt%2==0:
        if num<0:
            num=abs(num)
            if num>0:
                num=-num
    hap=hap+num
print(hap)

#----------모범답안----------
hap=0
i=1
while True:

num=int(input(str(i)+'번째 정수 입력: '))
    if i%2==0:
        num=-num
    hap=hap+num
    i=i+1

    if i>10:
        break
print('10개의 정수의 합: ',hap)