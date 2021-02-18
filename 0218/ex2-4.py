"""움직이는 물체의 운동에너지를 계산 하시오.
물체의 에너지를 계산하는 식은 0.5X무게X속도²"""
weight=int(input('물체의 무게를 입력하시오(킬로그램): '))
speed=int(input('물체의 속도를 입력하시오(미터/초): '))
energy=0.5*weight*(speed**2)
print('물체는','%.1f'%energy,'에너지를 가지고 있다')