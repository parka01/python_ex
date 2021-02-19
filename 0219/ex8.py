'''i = 0
while i <= 100:
    i=i+1
    if i%2==0 and i%3!=0:
        print(i)'''
print('1~100사이의 수 중에서 2의 배수이면서 3의 배수가 아닌 수: ',end='')
i=1
while i<=100:
    if(i%2==0)and(i%3!=0):
        print(i,end=',')
    i=i+1
