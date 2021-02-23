#수를 나열해서 첫째 마지막 비교해서 큰거 올리기 작은거 올리기
import random
list=set()
i=0
while True:
    list.add(random.randint(1,100))
    i=i+1

    if len(list)==10:
        break
print('생성된 집합: ',list)
sorted(list)
print('집합에서 가장 큰 수: ',list[10])
print('집합에서 가장 작은 수: ',list[0])
#----------답안----------
import random
lists=set()
while len(lists)<10:
    lists.add(random.randint(1,100))
temp=list(sorted(lists))
print('생성된 집합: ',lists)
print('집합에서 가장 큰 수: ',temp[len(temp)-1])
#print('집합에서 가장 큰 수: ',temp[-1])같다
print('집합에서 가장 작은 수: ',temp[0])
#일일이 값을 비교해서 가장 작은 수 큰 수 할 수 있다.