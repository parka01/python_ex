#for문을 이용한 구구단 출력
'''dan=int(input('출력을 원하는 단 입력: '))
print('***',dan,'단***')
for i in range(1,10):
    print(dan,'*',i,'=',dan*i)'''

#while문을 이용한 구구단 출력
'''dan=int(input('출력을 원하는 단 입력: '))
print('***',dan,'단***')
i=1
multi=0
while i<=9:
    multi=multi*i
    i=i+1
    print(dan,'*',i,'=',dan*i)'''

#----------while 사용한 모범답안----------
dan=int(input('출력을 원하는 단 입력: '))
print('***',dan,'단***')
i=1

while i<=9:
    print(dan,'*',i,'=',dan*i)
    i=i+1
