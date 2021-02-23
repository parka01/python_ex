#다음과 같은 튜플에서 중복된 숫자와 중복 횟수를 출력하고, 중복이 제거된
#요소를 리스트로 출력하는 프로그램을 작성하시오.
'''num=(1,2,4,4,2,3,7,7,9,3)
print('최초의 튜플: ',num)
empty_list=[]
for i in range(len(num)):
    if num[i] not in empty_list:
        print('중복된 숫자: ',num[i],',',num.count(num[i]),'회')
        empty_list.append(num[i])
minus=set(num)
list=list(minus)
print('중복이 제거된 리스트: ',list)'''

#----------모범답안----------
arr=(1,2,4,4,2,3,7,7,9,3)
alist=[] #리스트를 새로 하나 만든다.
#반복해야 한다. Array튜플에 있는 값을  alist에 넣는 작업을 반복해야 한다.
for i in range(len(arr)): #반복하는 횟수는 어레이의 길이만큼만 반복한다.
    if arr[i] not in alist: #alist에 값이 없는 경우에만 집어넣어라 if array에 i번째 값이 not in alist라면
        alist.append(arr[i]) #alist에 추가해라 arr의 i값을
        if arr.count(arr[i])>=2: #count했을 떄 2개 이상이면 추가를 하여라(2번이상 나온다면)
            print('중복된 숫자: ',arr[i],',',arr.count(arr[i]),'회') 
            #모든 반복문이 다끝나면 리스트에 중복안되는 값이 오름차순으로 들어간다.
            #for반복문을 나와서 alist를 정리한다.
alist.sort()
print('중복이 제거된 리스트: ',alist)
