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
>>> 