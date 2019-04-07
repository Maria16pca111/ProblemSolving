#return the count of values less than or equal to x

def Count_Values_x(array,k):
    count=0
    for x in array:
        if(x>k):
            count+=1
    return count
array=[1,4,8,12,4,6,2]
k=2
print(Count_Values_x(array,k))
                
