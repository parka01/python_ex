Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #score라는 사전을 한번 만들어 보자!
>>> score={202101:98,202102:88,202103:90} #key(학번):value(점수) 형식이다
>>> score
{202101: 98, 202102: 88, 202103: 90}
>>> type(score)
<class 'dict'>
>>> num={1:'a',2:'b',1:'c',2:'d'} #key값은 중복이 안된다 한번 보자.
>>> num
{1: 'c', 2: 'd'}
>>> #중복되는 경우에는 뒤에있는 값이 저장이 된다.
>>> empty=dict()
>>> empty
{}
>>> list1=[[1,'하나'],[2,'둘'],[3,'셋']]
>>> dic1=dict(list1)
>>> dic1
{1: '하나', 2: '둘', 3: '셋'}
>>> #사전형으로 바뀐 집합
>>> list2=[[1,2,3],[4,5],[7,8,9]]
>>> #list2=다중형식으로 만들어진 리스트
>>> list3=[202101,202102,202103]
>>> list4=[99,88,90]
>>> dic3=dict(zip(list3.list4))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dic3=dict(zip(list3.list4))
AttributeError: 'list' object has no attribute 'list4'
>>> dic3=dict(zip(list3,list4))
>>> dic3
{202101: 99, 202102: 88, 202103: 90}
>>> dic2=dict(list2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dic2=dict(list2)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> #list2의 요소가 [1,2,3]이런식으로 3개로 구성되어있으면 dict()를 이용하여 사전형으로 만들 수 없다.list1과 비슷한 형식인 [4,5]형은 가능
>>> dict1={1:'one',2:'two',3:'three'}
>>> dict1[1]
'one'
>>> dict1[4]='four'
>>> dict1
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> #새로운 'four'라는 멤버가 키값이 4인곳에 value가 저장이 되었다.
>>> del dict1[1]
>>> dict1
{2: 'two', 3: 'three', 4: 'four'}
>>> #키값 1번을 삭제하여 사라진 모습
>>> del dict1
>>> dict1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict1
NameError: name 'dict1' is not defined
>>> #dict1이 지워졌다.
>>> dict1={1:'one',2:'two',3:'three',4:'four'}
>>> 1 in dict1
True
>>> 'one' in dict1
False
>>> #사전자료형에서 in연산자는 key값만 사용이 가능하다.
>>> for i in dict1:
	print(dict1[i]) #dict1에 i요소가 있다면 그 i내용을 출력하여라

	
one
two
three
four
>>> max(dict1)
4
>>> sum(dict1)
10
>>> dict1.get(3)
'three'
>>> #get()메소드를 이용하면 사전안에 들어있는 키값을 이용해서 해당하는 value값을 검색 할 수 있다.
>>> dict1.get(5)
>>> 
>>> #5value가 없기 때문에 아무것도 나오지 않는다.
>>> dict2=dict1.copy()
>>> dict2
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> dict3=dict1
>>> dict3
{1: 'one', 2: 'two', 3: 'three', 4: 'four'}
>>> dict2.clear()
>>> dict2
{}
>>> dict1.setdefault(3)
'three'
>>> #setdefault()메소드를 이용하면 키값에 해당하는 value값을 볼 수 있다.
>>> dict1.pop(4)
'four'
>>> #key값4에 해당하는 value삭제
>>> dict1
{1: 'one', 2: 'two', 3: 'three'}
>>> dict1.popitem()
(3, 'three')
>>> #사전에서 임의의 값을 삭제해준다.
>>> dict1
{1: 'one', 2: 'two'}
>>> dict2={7:'seven',8:'eight'}
>>> dict1.update(dict2)
>>> dict1
{1: 'one', 2: 'two', 7: 'seven', 8: 'eight'}
>>> #dict1에 dict2가 추가되었다.
>>> dict2
{7: 'seven', 8: 'eight'}
>>> #keys()사전자료형에 있는 key값만 보여달라
>>> for num in dict1.keys():
	print(num,end=' ')

	
1 2 7 8 
>>> #end=' '옆으로 계속 출력을 하여라
>>> #values()를 사용하여 사전자료형에 있는 values값만 보여달라
>>> for alpa in dict1.values():
	print(alpa,end=' ')

	
one two seven eight 
>>> for num,alpa in dict1.items():
	print(num,'은 영어로: ',alpa,end=' ')

	
1 은 영어로:  one 2 은 영어로:  two 7 은 영어로:  seven 8 은 영어로:  eight 
>>> 
