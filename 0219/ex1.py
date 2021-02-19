num=int(input('합계를 원하는 숫자 입력: '))
i=1
sums=0
while i<=num:
    sums=sums+i
    i=i+1

print('1부터 %d까지의 합은: '%num,sums)
#----------------모범답안---------------------
'''num=int(input('합계를 원하는 숫자 입력: '))
i=1
sum=0
while i<=num:
    sum=sum+i
    i=i+1

print("1부터 {}까지의 합:{}".format(num,hap))'''