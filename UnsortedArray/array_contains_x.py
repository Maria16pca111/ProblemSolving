#Array Contains X
def indexarray(arr,x):
    index=-1
    count=0
    for i in arr:
        if(i==x):
            index=count
            break
        count+=1
        
    return index
arr=[1,2,3,4,5,6,7]
print(indexarray(arr,8))
        
