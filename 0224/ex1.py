a=int(input('숫자를 입력하시오: '))
b=int(input('또 다른 숫자를 입력하시오: '))

def plusNumber(a,b):
    total=a+b
    return total
total=plusNumber(a,b)
print('두 숫자의 합: ',total)