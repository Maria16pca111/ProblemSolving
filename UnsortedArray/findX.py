def findX(arr,x):
    flag=False
    for a in arr:
        if(arr[a]==x):
            flag=True
            print'x is availble in array'
    return flag
arr=[1,2,3,4,4,5,6]
print(findX(arr,8))