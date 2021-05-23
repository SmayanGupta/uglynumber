def prime(n):
    for i in range(2,n-1):
        if n%i==0:
            
            return False
        
        else:
            return True


print(prime(19))
print(prime(20))
           
def ugly(n):
    
    if(n%2==0) or(n%3==0) or (n%5==0):
        for i in range(6,n//2+1):
            if prime(i)==True:
                if n%i==0:
                    return False
                else:
                    return True
                
 
j=11
counter=10
#n=input('enter n')

#while j>10:
for j in range(16,60): 
    if ugly(j)==True:
        counter+=1
        if counter==15:
            print(j)
            break
            
    '''else:
        print('NÔOOOOOOO')'''
    #j+=1
