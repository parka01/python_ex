#다음과 같은 튜플을 생성하고, 각 요소가 튜플에 몇 번
#나타났는지를 출력하는 프로그램을 작성 하시오.
num=(1,3,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
print('생성된 튜플: ',num)
empty_list=[]
for i in range(len(num)):
    if num[i] not in empty_list:
        print(num[i],'개수: ',num.count(num[i]))
        empty_list.append(num[i])
