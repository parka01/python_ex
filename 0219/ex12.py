#while문을 이용한 구구단 출력
dan=2
while dan<=9: #9단까지 반복
    print('***',dan,'단***')
    i=1
    while i<=9: #각 단에서 1~9까지 반복
        if dan*i%2==0:
              print(dan,'*',i,'=',dan*i)
        i=i+1
    dan=dan+1
#-------for문을 이용한 구구단 출력-------
for dan in range(2,10):
    print('***',dan,'단***')
    for i in range(1,10):
        if dan*i%2==0:
              print(dan,'*',i,'=',dan*i)