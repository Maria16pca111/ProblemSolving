#Find the smallest array of an integer

def Smallest_Array(arr):
    Init_Small=arr[0]
    for x in arr:
        if(x<Init_Small):
            Init_Small=x
            
    return Init_Small
arr=[11,20,3,4,0]
print(Smallest_Array(arr))
