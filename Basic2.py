Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('한국','Seoul',2021)
한국 Seoul 2021
>>> print('한국','Seoul',2021,sep='-')
한국-Seoul-2021
>>> print('한국','Seoul');print('한국','Seoul')
한국 Seoul
한국 Seoul
>>> print('한국','Seoul',end='');print('한국','Seoul')
한국 Seoul한국 Seoul
>>> print('한국','Seoul',end=' ');print('한국','Seoul')
한국 Seoul 한국 Seoul
>>> #end=''줄 바꿈 없이 출력!
>>> print('Hi python')
Hi python
>>> print("Hi python")
Hi python
>>> print('"Hi python"')
"Hi python"
>>> print("'Hi python'")
'Hi python'
>>> print("Hi python"*5)
Hi pythonHi pythonHi pythonHi pythonHi python
>>> print("Hi python,"*5)
Hi python,Hi python,Hi python,Hi python,Hi python,
>>> print("Hi python, "*5)
Hi python, Hi python, Hi python, Hi python, Hi python, 
>>> print("당신의 나이는 {}세 입니다.".format(19))
당신의 나이는 19세 입니다.
>>> print('당신의 이름은 {}이고, 나이는 {}세 입니다.'.format('Ellia',19))
당신의 이름은 Ellia이고, 나이는 19세 입니다.
>>> print('{0}에 {0}을 더하면 {0}이 되고, {1}에 {0}을 더하면 {1}이 된다.'.format('정수','실수'))
정수에 정수을 더하면 정수이 되고, 실수에 정수을 더하면 실수이 된다.
>>> print('이름은 {name}이고, 나이는 {age}세이고, 주소는 {add}입니다.'.format(age=19,add='Busan',name='Ellia'))
이름은 Ellia이고, 나이는 19세이고, 주소는 Busan입니다.
>>> name=input('이름 입력: '); print('이름은{}'.format(name))
이름 입력: Ellia
이름은Ellia
>>> name=input('이름 입력: ');print('이름은 {}'.format(name))
이름 입력: Ellia
이름은 Ellia
>>> age=int(input('나이는: '));print('나이는{}'.format(age));print(type(name),type(age))
나이는: 19
나이는19
<class 'str'> <class 'int'>
>>> 
