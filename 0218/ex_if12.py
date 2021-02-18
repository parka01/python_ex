level=int(input('직급을 입력: '))
age=int(input('나이를 입력: '))
if level==7 or level==8:
    if age>=40 or age<=49:
        print('연금 80% 대상자입니다.')
elif level==5 or level==6:
    if age>=50 or age<=59:
        print('연금 100% 대상자입니다.')
else: 
    print('연금 대상자가 아닙니다.')
#----------------모범답안---------------------
level=int(input('직급: '))
age=int(input('나이: '))
if(level==7 or level==8) and (40<=age<=49):
    print('연금 80% 대상자')
elif(level==5 or level==6) and (50<=age<=59):
    print('연금 100%대상자')
else:
    print('연금 대상자 아님')