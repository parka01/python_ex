import random
#빈 집합을 일단 만들어 보자
num1=set()
num2=set()
while True: #무한반복 시켜놓고
    if len(num1)<10: #만약에 num1의 길이가 10보다 작다면
        num1.add(random.randint(1,100))#집합에는 append가 아니라 add를 사용
    if len(num2)<10:
        num2.add(random.randint(1,100))#무한반복은 얘네의 길이가 10개면 중단.
    if len(num1)==10 and len(num2)==10:
        break
print('발생된 10개의 난수 num1: ',num1)
print('발생된 10개의 난수 num2: ',num2)
print('num1,num2의 합집합: ',num1&num2)
print('num1,num2의 교집합: ',num1|num2)
print('num1,num2의 차집합: ',num1-num2)