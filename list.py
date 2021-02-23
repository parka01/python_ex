Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1=[1,2,3,4]
>>> list2=[1,'one',(1,2,3)]
>>> st='python'
>>> list3=list(st)
>>> list3
['p', 'y', 't', 'h', 'o', 'n']
>>> list1[2]=(1,2,3)
>>> list1
[1, 2, (1, 2, 3), 4]
>>> del list1[0]
>>> list1
[2, (1, 2, 3), 4]
>>> sum(list1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    sum(list1)
TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
>>> list1
[2, (1, 2, 3), 4]
>>> list3=[1,2,3,4]
>>> 
================================ RESTART: Shell ================================
>>> list1=[1,2,3,4]
>>> list1.append((1,2,3))
>>> list1
[1, 2, 3, 4, (1, 2, 3)]
>>> list1.insert(2,'kor')
>>> list1
[1, 2, 'kor', 3, 4, (1, 2, 3)]
>>> list1.append(100)
>>> list1
[1, 2, 'kor', 3, 4, (1, 2, 3), 100]
>>> list1.extend('python')
>>> list1
[1, 2, 'kor', 3, 4, (1, 2, 3), 100, 'p', 'y', 't', 'h', 'o', 'n']
>>> list1.extend(range(100,105))
>>> list1
[1, 2, 'kor', 3, 4, (1, 2, 3), 100, 'p', 'y', 't', 'h', 'o', 'n', 100, 101, 102, 103, 104]
>>> 
============================== RESTART: Shell =============================
>>> cities=['seoul','busan','daegu','daejeon']
>>> last_city=cities.pop()
>>> last_city
'daejeon'
>>> type(last_city)
<class 'str'>
>>> type(cities)
<class 'list'>
>>> cities
['seoul', 'busan', 'daegu']
>>> first_city=cities.pop(0)
>>> first_city
'seoul'
>>> cities
['busan', 'daegu']
>>> cities.remove('busan')
>>> cities
['daegu']
>>> cities.clear()
>>> cities
[]
>>> 
============================== RESTART: Shell =============================
>>> num1=[33,44,11,22,77,88,55]
>>> num1.index(11)
2
>>> num1.sort()
>>> num1
[11, 22, 33, 44, 55, 77, 88]
\
>>> num1.sort(reverse=True)
>>> num1
[88, 77, 55, 44, 33, 22, 11]
>>> 
============================== RESTART: Shell =============================
>>> num[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    num[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]
NameError: name 'num' is not defined
>>> num=[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]
>>> for j in range(len(num)):
	sum=0
	for i in range(len(num[j])):
		sum=sum+num[j][i]
		print(j+1,'번째 줄의 합: ',sum)

		
1 번째 줄의 합:  11
1 번째 줄의 합:  23
1 번째 줄의 합:  36
2 번째 줄의 합:  21
2 번째 줄의 합:  43
2 번째 줄의 합:  66
3 번째 줄의 합:  31
3 번째 줄의 합:  63
3 번째 줄의 합:  96
3 번째 줄의 합:  130
4 번째 줄의 합:  41
4 번째 줄의 합:  83
>>> 
>>> num=[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]
>>> for j in range(len(num)):
	sum=0
	for i in range(len(num[j])):
		sum=sum+num[j][i]
	print(j+1,'번째 줄의 합: ',sum)
	
SyntaxError: multiple statements found while compiling a single statement
>>> num=[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]

>>> for j in range(len(num)):
	sum=0
	for i in range(len(num[j])):
		sum=sum+num[j][i]
	print(j+1,'번째 줄의 합: ',sum)
	
SyntaxError: multiple statements found while compiling a single statement
>>> num=[[11,12,13],[21,22,23],[31,32,33,34],[41,42]]
>>> for j in range(len(num)):
	sum=0
	for i in range(len(num[j])):
		sum=sum+num[j][i]
	print(j+1,'번째 줄의 합: ',sum)

	
1 번째 줄의 합:  36
2 번째 줄의 합:  66
3 번째 줄의 합:  130
4 번째 줄의 합:  83
>>> num=int(input('숫자를 입력: '))
숫자를 입력: 5
>>> list(num)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    list(num)
TypeError: 'int' object is not iterable
>>> s1=list(num)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    s1=list(num)
TypeError: 'int' object is not iterable
>>> num=int(input('숫자를 입력: '))
숫자를 입력: 5
>>> s1=list(num)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    s1=list(num)
TypeError: 'int' object is not iterable
>>> type(num)
<class 'int'>
>>> s1=str(num)
>>> s1
'5'
>>> s1=list(num)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s1=list(num)
TypeError: 'int' object is not iterable
>>> s1
'5'
>>> 
============================== RESTART: Shell =============================
>>> t1=(1,2,3,4)
>>> t2=11,22,33,44
>>> type(t1),type(t2)
(<class 'tuple'>, <class 'tuple'>)
>>> #괄호가 없어도 튜플 형식이다.
>>> t1[2]
3
>>> t1[2]=20
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    t1[2]=20
TypeError: 'tuple' object does not support item assignment
>>> #튜플에 추가할 수 가 없다.
>>> lan='python'
>>> t3=tuple(lan)
>>> type(t3)
<class 'tuple'>
>>> t3
('p', 'y', 't', 'h', 'o', 'n')
>>> t1=(1,2,[10,20,30])
>>> t12[2][1]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    t12[2][1]
NameError: name 't12' is not defined
>>> t1[2][1]
20
>>> 
============================== RESTART: Shell =============================
>>> color=('white','red','yellow','black')