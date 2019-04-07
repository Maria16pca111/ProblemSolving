#Return the Indices of Values which adds upto x


def Subset_Pair_X(A,a,X):    
    for x in A:
        for y in a:
            if(x+y==X):
                print x,y
    return 0             
def subset_adds_return_indices(array1,array2,x):
    Count=0
    for x in array1:
        for y in array2:
            if(Subset_Pair_X(array1,array2,x)==True):
                Count+=1
                print(array1[x],array2[y])
    return False
array1=[1,2,3,4,5]
array2=[1,3,5,6]
x=4
subset_adds_return_indices(array1,array2,x)
    
