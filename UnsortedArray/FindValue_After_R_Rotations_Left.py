# find the value after the r rotations left 

def Value_After_R_Rotations_Left(a,k):
    count=0
    while(count!=k):
        x=a.pop(-1)
        count+=1
        a.insert(0,x)
    count+1
    return a,a[Index]
    
a=[1,2,3,4,5,6,7,8,9]
k=5
Index=3
print(Value_After_R_Rotations_Left(a,k))