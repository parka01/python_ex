#다음 5과목의 점수의 총점과 평균을 구하는 프로그램을 작성하시오.
sub1=int(input('국어: '))
sub2=int(input('수학: '))
sub3=int(input('사회: '))
sub4=int(input('과학: '))
sub5=int(input('영어: '))
total=float(sub1+sub2+sub3+sub4+sub5)
average=total/5
print(average)