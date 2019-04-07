# sum of all elements in a

def sumArray(arr):
    sum=0
    for x in arr:
        sum=sum+x
    return sum
arr=[1,2,3,4,5,9]
print(sumArray(arr))