#return the no of times found in x

def number_times(arr,x):
    count=0
    
    for i in arr:
        if i==x:
            count+=1        
    return count   
arr=[1,2,3,4,3,1]

print(number_times(arr,1))

        