#found the no of times smallest integer is found in array
def smallest_count(array):
    smallest=array[0]
    count=0
    for arr in array:               
        if(arr<smallest):
            arr=smallest
            count+=1
    return count
array=[5,8,7,1,2,3,2,1,1,1]
print(smallest_count(array))

            


