#사용자로부터 3개의 숫자를 입력받아 가장 큰 수를 구하는 프로그램을
#작성하시오. 3개의 숫자를 매개변수로 받아서 가장 큰 수를
# 반환하는 부분을 findMax(a,b,c)함수로 작성시오.
def findMax(a,b,c):
    if a>b:
        biggest=a
    else:
        biggest=b
    if biggest<c:
        biggest=c
    return biggest

a=int(input('첫 번째 숫자: '))
b=int(input('두 번째 숫자: '))
c=int(input('세 번째 숫자: '))

biggest=findMax(a,b,c)
print('가장 큰 값은: ',biggest)