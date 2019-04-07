#found the no of times largest integer is found in array

def Largest_Array(arr):
    Init_Large=arr[0]
    for x in arr:
        if(x>Init_Large):
            Init_Large=x
    return Init_Large

def Largest_Array_Count(arr):
    count=0
    for x in arr:
        if(Largest_Array(arr)==x):
            count+=1
        
    return count,Largest_Array(arr)
arr=[1,2,3,4,5,5,5,1]
print(Largest_Array_Count(arr))

