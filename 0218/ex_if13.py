age=int(input('나이를 입력: '))
height=int(input('키(cm)를 입력: '))
if age>=8:
    if height>=120:
        print('고속 롤러코스터 입장 가능!')
    else:
        print('저속 롤러코스터 입장 가능!')
else:
    print('입장할 수 없습니다.')
#----------------모범답안---------------------
age=int(input('나이 입력: '))
if age>=8: #나이가 8세 이상인 경우에만 키 입력
    height=int(input('키 입력(cm): '))
    if height >=120:
        print('고속 롤러코스터 탑승 가능!')
    else:
        print('저속 롤러코스터 탑승 가능!')
else:
    print('입장불가!')