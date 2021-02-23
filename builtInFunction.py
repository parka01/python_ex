Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='123'
>>> type(s),s
(<class 'str'>, '123')
>>> a=int(s)
>>> type(a),a
(<class 'int'>, 123)
>>> e=str(a)
>>> type(e),e
(<class 'str'>, '123')
>>> #절대값 구하는 법
>>> abs(-10)
10
>>> abs(10)
10
>>> t1=divmod(10,3)
>>> t1
(3, 1)
>>> type(t1)
<class 'tuple'>
>>> #몫과 나머지를 구해주는 내장함수임을 알 수 있다.
>>> pow(2,4)
16
>>> t2=pow(2,3)
>>> t2
8
>>> type(t2)
<class 'int'>
>>> #정수와 지수승의 값을 지정해서 계산해주는 내장함수
>>> round(4,6)
4
>>> round(4.6)
5
>>> #반올림 해준다.
>>> oct(65536)
'0o200000'
>>> #8진법으로 나타내주는 내장함수
>>> chr(97)
'a'
>>> #아스키 코드에 따른 출력값이다.
>>> ord('a')
97
>>> chr(45824),chr(54620)
('대', '한')
>>> dic1=dict(enumerate('abcd'))
>>> dic1
{0: 'a', 1: 'b', 2: 'c', 3: 'd'}
>>> s='the best language is Python'
>>> len(s)
27
>>> a=1234
>>> len(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    len(a)
TypeError: object of type 'int' has no len()
>>> #에러가 나는 이유는 글자수를 알려주는 내장함수 len()은 위와같이 문자열에만 쓸 수 있기 때문.
>>> max(s)
'y'
>>> min(s)
' '
>>> #s의 아스키코드의 최대값=y 최소값=공백 출력
>>> max([1,2,3,4,5])
5
>>> min([1,2,3,4,5])
1
>>> sum([1,2,3,4,5])
15
>>> sum(1,2,3,4,5)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sum(1,2,3,4,5)
TypeError: sum() takes at most 2 arguments (5 given)
>>> list1=sorted((33,22,44,88,77,99))
>>> list1
[22, 33, 44, 77, 88, 99]
>>> type(list1)
<class 'list'>
>>> #원래는 ()괄호형식인 튜플타입이었지만 sorted하고나서 list타입으로 바뀌었다.
>>> list2=sorted(('Python'))
>>> type(list2)
<class 'list'>
>>> list2
['P', 'h', 'n', 'o', 't', 'y']
>>> type(list2)
<class 'list'>
>>> zip('123',('kim','lee','park'))
<zip object at 0x10c6ad780>
>>> list(zip('123',('kim','lee','park')))
[('1', 'kim'), ('2', 'lee'), ('3', 'park')]
>>> #튜플이 list타입으로 zip된 상태이다.
>>> list(zip('1230',('kim','lee','park')))
[('1', 'kim'), ('2', 'lee'), ('3', 'park')]
>>> #0은 빼먹고 리스트타입 속 튜플형식으로 zip되었다.
>>> list(zip('123',('kim','lee','park','choi')))
[('1', 'kim'), ('2', 'lee'), ('3', 'park')]
>>> #위와 마찬가지로 choi값을 뺴고 zip되었다.
>>> 