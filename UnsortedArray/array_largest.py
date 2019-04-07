#Find the largest array of an integer

def Largest_Array(arr):
    Init_Large=arr[0]
    for x in arr:
        if(x>Init_Large):
            Init_Large=x
    return Init_Large
arr=[11,20,3,4,0]
print(Largest_Array(arr))
