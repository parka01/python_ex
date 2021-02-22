#1부터 1000사이의 소수를 구하여 리스트에 저장한 다음
#소수와 소수의 개수를 출력하는 프로그램을 작성하시오.

num=1000
pnum=[] 
for i in range(1,num+1):
    dcnt=0 
    for j in range(1,i+1):
        if i%j==0:
            dcnt=dcnt+1
    if dcnt==2:
        pnum.append(i)
print('1부터 1000사이의 소수의 리스트: ',pnum)
print('1부터 1000사이의 소수의 개수: ',len(pnum))