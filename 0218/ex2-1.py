"""사용자로부터 두 개의 정수를 받아서 정수의 합, 차, 곱, 평균, 큰수, 작은 수를
계산하여 출력하는 프로그램을 작성 하시오. (파이썬 내장 함수 활용)"""
num1=int(input('x: '))
num2=int(input('x: '))
print('두 수의 합: ',num1+num2)
print('두 수의 차: ',num1-num2)
print('두 수의 곱: ',num1*num2)
print('두 수의 평균: ',(num1+num2)/2)
print('큰 수: ',max(num1,num2))
print('작은 수: ',min(num1,num2))