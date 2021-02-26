Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1='i like python'
>>> s2='I love Python'
>>> s3='''i really love python'''
>>> s4='''i like python
i love python
i really like python'''
>>> print(s1,s2,s3)
i like python I love Python i really love python
>>> print(s4)
i like python
i love python
i really like python
>>> s5=''
>>> s6=str()
>>> len(s5)
0
>>> s1=str(1234)
>>> s1
'1234'
>>> type(s1)
<class 'str'>
>>> s2=str(123.456)
>>> s2
'123.456'
>>> s3=str([1,2,3])
>>> s3[0]
'['
>>> s4=str((1,2,3))
>>> s4[2]
','
>>> s1='i like python language'
>>> s2=s1.capitalize()
>>> s2
'I like python language'
>>> s3=s1.title()
>>> s3
'I Like Python Language'
>>> s4=s1.upper()
>>> s4
'I LIKE PYTHON LANGUAGE'
>>> s5=s4.lower()
>>> s5
'i like python language'
>>> s1='i like python'
>>> s2=s1.center(30)
>>> s2
'        i like python         '
>>> s3=s1.center(30,'*')
>>> s3
'********i like python*********'
>>> s4=s1.ljust(30,'*')
>>> s3
'********i like python*********'
>>> s4
'i like python*****************'
>>> s1.count('i')
2
>>> s5='i like python language'
>>> #인덱스번호 0부터 12까지 a라는 문자열이 몇개인지 출력하는 법
>>> s5.count('a',0,12)
0
>>> s5.count('a',0,16)
1
>>> #인덱스번호 12이후에 a가 몇개인지 출력하는 법
>>> s5.count('a',12)
2
>>> #특정 원하는 문자가 가장 나중에 나타난 자리 출력하기
>>> s1='i like python language'
>>> s1.rindex('i')
3
