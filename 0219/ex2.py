num1=int(input('첫 번째 숫자 입력: '))
num2=int(input('두 번째 숫자 입력: '))
i=min([num1,num2])
i2=max([num1,num2])
sums=0
while i<=num:
    sums=sums+i
    i=i+1

#----------------모범답안---------------------
first=int(input('첫 번째 숫자 입력: '))
second=int(input('두 번째 숫자 입력: '))
if first>second:
    temp=first
    first=second
    second=temp
print(first,'부터',second,'까지의 합은: ',end='')

sum=0
while first<=second:
    sum=sum+first
    first=first+1
print(sum)
