def func1(a,b): #a,b는 함수이기때문에 지역변수
    c=a+b   #c: 지역변수이다.
    print('x,y의 값은: ',x,y) #전역변수x,y가 출력

def func2(x,y):
    x=x*2
    y=y*2
    print('x,y의 값: ') #여기에서는 지역변수가 나옴.
    global z #global이라고 붙였기 때문에 전역변수이다.
    z=x*y
#메인 프로그램
x=10 #x,y전역변수이다.
y=20
fumc1(x,y) 
#c는 지역변수이기때문에 print(c)가 먹히지 않는다.

func2(x,y)
print(x,y) #전역변수출력
print(z) #func2에서 선언된 global변수 z값이 나온다.
