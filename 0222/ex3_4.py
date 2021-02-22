hap=0
i=1

while True:
    hap=hap+i

    if i%10==0:
        print('1-',i,':',hap)
        
    i=i+1
    if i>100:
        break