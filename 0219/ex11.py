num=int(input('숫자를 입력하시오!'))
i=0
for i in range(0,num):
    i=i+1
    print(i*'*')

#----------모범답안---------
num=int(input("숫자입력:"))
i=1
while i<=num:
    j=1
    while j<=i: 
        print("*",end='')
        j=j+1
    print()
    i=i+1
#----------내 답안의 추가 수정 답안---------
num=int(input('숫자를 입력하시오!'))
for i in range(1,num+1):
    print(i*'*')
#----------별거꾸로 답안---------
num=int(input('숫자를 입력하시오!'))
for i in range(num,0,-1):
    print(i*'*')
#----------거꾸로 추가답안---------
num=int(input("숫자입력:"))
while num>=1:
    j=1
    while j<=num: 
        print("*",end='')
        j=j+1
    print()
    num=num-1