"""원기둥의 부피를 계산하는 프로그램을 작성 하시오. 원기둥의
부피는 V=π²h 이다."""
r=int(input('r: '))
h=int(input('h: '))
v=int(3.14*r**2*h)
print('원기둥의 부피: ','%.1f'%v)

#---------모범답안-----------------
import math
r = float(imput("r: "))
h = float(imput("r: "))
vol = math.pi*r**2*h
print( "원기둥의 부피: ",vol)