# find the two unsorted array is same if same returns true if not returns false

def Array_Compare(arr1,arr2):
    flag=False
    if(len(arr1)==len(arr2)):
        for x in arr1:
            for y in arr2:
                if(x==y):
                    flag=True
    return flag           
arr1=[1,2,3,4,5,6,7]
arr2=[1,2,3,4,5,6,7]
print(Array_Compare(arr1,arr2))