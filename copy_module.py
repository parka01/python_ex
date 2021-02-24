Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import copy
>>> list1=[1,2,3]
>>> list2=list1
>>> id(list1),id(list2)
(1785338102464, 1785338102464)
>>> list1[0]=100
>>> list1,list2
([100, 2, 3], [100, 2, 3])
>>> list3=[1,2,3]
>>> list4=copy.copy(list3)
>>> id(list3),id(list4)
(1785371257728, 1785371257024)
>>> list3[0]=100
>>> list3,list4
([100, 2, 3], [1, 2, 3])
>>> #copy.copy()모듈은 한번만 복붙이라 업뎃이 반영되지 않는다.