gender=input('당신의 성별은(M또는 F): ')
height=input('키는? ')
weight=input('몸무게는? ')
Mweight=height*height*22
Fweight=height*height*21
if gender==M:
    if weight+weight*0.2 >=110:
        if weight+weight*0.2 >=120:
            print('비만체중')
        else:
            print('과체중')
        


#----------------모범답안---------------------
gen=input('성별('M or m'또는 'F or f'): ')
height=float(input('키입력(cm)'))/100
weight=float(input('몸무게 입력(kg)'))
if (gen=='M' or gen=='m'): #남자일 경우
    avg=height*height*22
    if 110<=weight/avg*100<=119:
        print('과체중')
    elif weight/avg*100>=120:
        print('비만체중')
    else:
        print('표준체중')
elif (gen=='F' or gen=='f'): #여자일 경우
       avg=height*height*21
    if 110<=weight/avg*100<=119:
        print('과체중')
    elif weight/avg*100>=120:
        print('비만체중')
    else:
        print('표준체중')
else: print('성별 입력이 잘못 되었습니다.')
