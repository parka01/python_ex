#for문을 이용한 1000이내 배수의 합 출력
'''num=int(input('합을 원하는 입력: '))
print('1부터 1000까지 %d의 배수의 합은: '%num,end='')
for i>=0 and num in range(1,10001):
    num=num*i
    i=i+1
print(num)'''

#----------모범답안----------
num=int(input('합을 원하는 배수 입력: '))
hap=0

for i in range(0,1001,num): #0자리에 i넣어도 된다.
    hap=hap+i
'''print('1~1000까지의 {}의 배수의 합은: {}'.format(num,hap))'''
print('1~1000까지의 %d의 배수의 합은: %d',%num%hap)