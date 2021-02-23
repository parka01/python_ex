def morning1(name): #함수정의하고나서 반환값이 없다.
    print(name,'씨 굿모닝 입니다.')
    #name이라는 매개변수를 받아서 print문을 출력


def morning2(name): #name이라는 형식 매개변수가 필요
    s=name+'씨 굿모닝 입니다.'
    return s    #리턴값이 한개인 함수, 메인 프로그램에서 출력 콘솔창X


def morning3(name): 
    s1='오늘 날씨 쾌청'
    s2=name+'굿모닝 입니다.'
    return s1, s2
    #반환값이 2개이다.

#여기까지 3개의 함수를 정의를 해 보았다.

#메인프로그램
morning1('파이썬')
s=morning2('파이썬')
print(s)
s1,s2=morning3('파이썬')
print(s1,s2)