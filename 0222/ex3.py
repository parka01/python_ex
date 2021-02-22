#다음과 같은 2차원 다중리스트가 있을 때, 각 줄의 합을 출력하고, 모든 요소
#중에서 가장 작은 값을 구하는 프로그램을 작성하시오. 
#최소값을 구하는 min()함수와 합을 구하는 sum()함수를 사용하시오.

list1=[[11,33,22,7],[77,2,90],[3,66,44,9,8]]

minvalue=min(list1[0]) #list1의 인덱스0번의 min값

for i in range(len(list1)):
    print((i+1),'번째 줄 합계: ',sum(list1[i]))
    if minvalue > min(list1[i]):
        minvalue=min(list1[i])
print('리스트에서 가장 작은 값은: ',minvalue)