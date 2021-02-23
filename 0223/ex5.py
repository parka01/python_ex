'''num=int(input('숫자를 입력하시오: '))
a=a for i in range(1, num+1) 
if i % 2 == 0:
b=b for i in range(1, num+1)
if i % 3 == 0:
c=c for i in range(1, num+1)
if i % 7 == 0:
d=d for i in range(1, num+1)
if i %(2*3*7) == 0:
print('2의 배수: ',a)
print('3의 배수: ',b)
print('7의 배수: ',c)
print('2,3,7의 배수: ',d)'''
#----------모범답안----------
num=int(input('숫자를 입력하시오: '))
nul_2=set()
nul_3=set()
nul_7=set()
for i in range(1,num+1):
    if(i%2==0):
        nul_2.add(i)
    if(i%3==0):
        nul_3.add(i)
    if(i%7==0):
        nul_7.add(i)
print('2의 배수: ',sorted(nul_2))
print('3의 배수: ',sorted(nul_3))
print('7의 배수: ',sorted(nul_7))
print('2,3,7의 배수: ',sorted(nul_2&nul_3&nul_7))