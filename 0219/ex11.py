num=int(input('숫자를 입력하시오!'))
i=0
for i in range(0,num):
    i=i+1
    print(i*'*')

#----------모범답안---------
num=int(input('숫자입력: '))
i=1
while i<=num: #줄 수를 증가하기 위한 반복문
    j<=i:
    print('*',end='')
    j=j+1
    print() #줄 바꿈 프린트문
    i=i+1
#----------추가답안---------
num=int(input('숫자를 입력하시오!'))
for i in range(1,num+1):
    print(i*'*')
#----------추가답안---------
num=int(input('숫자를 입력하시오!'))
for i in range(num,0,-1):
    print(i*'*')
#----------추가답안---------
num=int(input('숫자를 입력하시오!'))

while num<=1: #줄 수를 증가하기 위한 반복문
    j<=num:
    print('*',end='')
    j=j+1
    print() #줄 바꿈 프린트문
    num=num-1