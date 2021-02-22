num1=int(input('숫자를 입력해봐: '))
num2=int(input('또 숫자를 입력해봐: '))

hap=0

if num1>num2:
    temp=num1
    num1=num2
    num2=temp
for i in range(num1,num2+1):
    if i%2!=0:
        hap=hap+i
print(num1,"부터",num2,'까지 홀수의 합은',hap,'이란다.')