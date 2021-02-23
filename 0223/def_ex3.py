def changeData1(x,y): #정수를 매개변수로 사용
    x=x+y
    print('x값은: ',x)

def changeData2(num): #리스트를 매개변수로 사용
    num[1]=200
    print(num)

#메인 프로그램

a=10 #실매개변수10값이 ㅣ1줄의 changeData1(x,y)인 형식변수에 사용
b=20
changeData1(a,b)
print(a)
list1=[10,20,30]
changeData2(list1)
print(list1)