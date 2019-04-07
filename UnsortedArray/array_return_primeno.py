#return the no of primeno in an array
import math
def IsPrime(n):
    flag=True
    for i in range(2,n**1/2):
        if(n%i==0):
                flag=False
                break                
    return flag

def array_contain_prime(arr):        
        flag=False        
        for x in arr:
                if(IsPrime(x)):
                        flag=True
                        print(x)
        return flag

arr=[1,2,5,6,7,11,15]
# arr = int(raw_input('Enter how many elements you want: '))
# for i in range(0, arr):
#     x = raw_input('Enter the numbers into the array: ')
print(array_contain_prime(arr))


