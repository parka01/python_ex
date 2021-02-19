num=int(input('팩토리얼을 원하는 배수 입력: '))
#(num,0,-1)
for i in range(1,num+1,1): #num값에서 -1씩 감소해서 0+1까지
    result=num*i
print(result)
4321

num=int(input('팩토리얼 숫자 입력: '))
for i in range(num,0,-1):
    fac=fac*i
print('%d의 팩토리얼 값은: '%num,fac)