def BigSmall(a,b): #함수정의(호출전에 정의)
    if a>b:
        big=a
        small=b
    else:
        big=b
        small=a
    return big,small #함수결과를 반환하라
a=int(int(input('첫 번째 숫자 입력: ')))
b=int(int(input('두 번째 숫자 입력: ')))
#return에 나온 전달값을 받기위한 변수가 필요하다.
x,y=BigSmall(a,b) #함수를 호출하고 결과 값은 x,y변수에 저장
print('큰 값: ',x)
print('작은 값: ',y)