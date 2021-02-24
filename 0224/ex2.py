num=int(input('출력을 원하는 단 입력: '))

def dan(num):
    i=1
    while i<=9:
        result=num*i
        print(num,'*',i,':',result)
        i=i+1
    return result
result=dan(num)


'''def total():
    dan=0
    while True:
        plus=dan+dan*i
        return plus
plus=total()'''

'''print('구구단 결과의 합: ',plus)'''
#----------모범답안----------
def gugudan(a):
    hap=0
    for i in range(1,10): #구구단 출력
        print(a,'*',i,'=',a*i)
    for j in range(1,10):
        hap=hap+(a*j)
    return hap

#메인프로그램
dan=int(input('단 입력: '))
total=gugudan(dan)
print(dan,'의 결과의 합: ',total)