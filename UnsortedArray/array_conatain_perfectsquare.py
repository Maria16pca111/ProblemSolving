#find the elements of array whether it is perfect or not,if perfect print the perfect no
import math
def perfectsquare_array(a):
    count=0
    for i in a:
        x=math.sqrt(i)
        m=round(x)
        if(m-x==0):
            print(i)
            count+=1
    return count
a=[1,2,3,4,6,16] 
print(perfectsquare_array(a))
