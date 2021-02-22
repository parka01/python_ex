#1부터 사용자가 입력한 숫자 사이의 소수의 리스트와 개수가 몇 개인지를
#출력하는 프로그램을 작성하시오.

num=int(input('숫자를 입력: '))
pnum=[] #빈 리스트를 생성
for i in range(1,num+1):
    dcnt=0 #약수의 개수
    for j in range(1,i+1):
        if i%j==0:
            dcnt=dcnt+1
    if dcnt==2:
        pnum.append(i)
print('1부터 ',num,'까지의 소수의 리스트: ',pnum)
print('1부터 ',num,'까지의 소수의 개수: ',len(pnum))