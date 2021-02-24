#find모듈 생성
def findMax(a,b,c):
    if a>b:
        biggest=a
    else:
        biggest=b
    if biggest<c:
        biggest=c
    return biggest

def findMin(a,b,c):
    if a<b:
        smallest=a
    else:
        smallest=b
    if smallest>c:
        smallest=c
    return smallest

def findSum(a,b,c):
    return a+b+c