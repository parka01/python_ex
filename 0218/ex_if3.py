import math
kor=int(input('국어 점수를 입력: '))
eng=int(input('영어 점수를 입력: '))
mat=int(input('수학 점수를 입력: '))

avg=(kor+eng+mat)/3
if avg>=95:
    print('당신의 평균은 %.2f 입니다.'%avg)
    print('축하합니다. A입니다.')
print('감사합니다.') #조건과 관계없이 항상 실행