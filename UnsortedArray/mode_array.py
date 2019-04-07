def mode_array(arr):
    count=0
    countmax=0  
    mode=0  
    for i in arr:
        count=0
        for j in arr:
            if(i==j):
                count+=1

        if(count>countmax):
            countmax=count
            mode=i

    return mode
arr=[5,8,3,2,3,3,3,2,6,9]
print(mode_array(arr))
            
            

