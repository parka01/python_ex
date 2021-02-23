import random
#중복을 허용하지 않는 6개의 값을 집어넣을 빈 집합을 먼저 만들어야 한다.
#총 중복 된 수가 몇개인지 확인해야 한다. 
lotto=set()
i=0
while True:
    lotto.add(random.randint(1,45)) #1부터 45까지의 랜덤숫자를 더한다.
    i=i+1

    if len(lotto)==6:
        break
print('이번주 로또 넘버: ',sorted(lotto))
print('중복된 난수의 발생 횟수: ',i-6)