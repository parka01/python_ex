import random
num=[]

for i in range(10): #10번 반복하여라
    num.append(random.randint(1,100))
print('리스트: ',num)
print('가장 큰 값: ',max(num))
print('가장 작은 값: ',min(num))
print('전체의 합: ',sum(num))
num.sort()
print('정렬된 리스트: ',num)