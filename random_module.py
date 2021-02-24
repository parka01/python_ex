Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> print(random.randint(1,100))
9
>>> #randint()정수난수를 발생시키는 함수
>>> print(random.randrange(10))
5
>>> #randrange(10) 0에서 10까지 정수난수 생성
>>> print(random.randrange(1,100))
50
>>> #1에서 10까지 정수난수 생성
>>> print(random.randrange(1,100,2))
73
>>> print(random.random())
0.21536884623149188
>>> print(random.uniform(100.1,100.2))
100.17805061570085
>>> #100.1에서 100.2사이의 랜덤수를 생성
>>> s='Python'
>>> print(random.choice(s))
h
>>> #문자열에서 임의의 문자 반환
>>> #리스트 항목에서도 사용 가능
>>> color=['red','green','blue']
>>> print(random.choice(color))
red
>>> #튜플에서 임의의 항목을 반환하기
>>> num=(1,2,3,4,5)
>>> print(random.choice(num))
4
>>> #물론 리스트에서도 임의의 항목을 반환할 수 있다.
>>> list1=[1,2,3,4,5]
>>> print(random.choice(list1))
4
>>> #shuffle()함수를 사용해 보자!
>>> print(random.shuffle(list1))
None
>>> random.shuffle(list1)
>>> print(list1)
[4, 2, 1, 3, 5]
>>> #리스트 내용물이 마음대로 섞인것을 확인할 수 있다.