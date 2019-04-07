#exercise 6

def loc_Array_value(arr,x):
    index=0
    count=0
    for i in arr:
        if(i==x):
            index=count
        count+=1
    return index
arr=[1,2,3,5,5,2,1,4]
print(loc_Array_value(arr,5))