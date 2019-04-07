#return the even no in an array of elements

def evenno_array(arr):
    flag=False
    for x in arr:
        if(x%2==0):
            flag=True
            print(x)
    return flag
arr=[1,3,4,5,5,7,2,10]
print(evenno_array(arr))