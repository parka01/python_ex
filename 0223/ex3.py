phone={}
for i in range(5): #단순하게 반복할 때
    id=(int(input(str(i+1)+'번째 학생 학번 입력: ')))
    pnum=(input(str(i+1)+'번째 학생 전화번호: '))
    phone[id]=pnum
print('학생 전화번호부가 완성되었습니다.')

id=int(input('검색을 원하는 학번: '))

if id in phone:
    print('입력한 학생의 전화번호: '+phone[id])
    #print('입력한 학생의 전화번호: '+phone.setdefault(id))똑같이 검색이 된다.
else:
    print('입력한 학생의 전화번호가 없습니다.')