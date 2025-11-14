n=[]
for i in range(10):
    if i>0 and i<9:
        print(' '*(9-i),'*')
    elif i==9 or i==0:
        j=0
        k=10
        while j<k:
            n.append('*')
            print(n[j],end='')
            j+=1    
