#length of the Array Questions

def lengthofarray(arr):
    count=0
    for _ in arr:
        count+=1
    return count
arr=[1,2,3,4,5,6,2,1,3,4]
print(lengthofarray(arr))