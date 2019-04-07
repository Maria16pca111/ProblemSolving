#array contains more than once 
def more_than_once(arr,x):
    flag=False
    count=0
    for i in arr:
        if i==x:
            count+=1
            if count>1:
                flag=True
    return flag
arr=[5,2,7,3,1]
print(more_than_once(arr,2))