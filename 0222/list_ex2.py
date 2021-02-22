#다음과 같은 튜플에서 중복된 숫자와 중복 횟수를 출력하고, 중복이 제거된
#요소를 리스트로 출력하는 프로그램을 작성하시오.
num=(1,2,4,4,2,3,7,7,9,3)
print('최초의 튜플: ',num)
empty_list=[]
for i in range(len(num)):
    if num[i] not in empty_list:
        print('중복된 숫자: ',num[i],',',num.count(num[i]),'회')
        empty_list.append(num[i])
minus=set(num)
list=list(minus)
print('중복이 제거된 리스트: ',list)