# Find the value which will be in index and get after R Rotations to the Right

def Index_R_Rotations_Find_I(a,I,R):
    rotation=1
    while(rotation<R):
        x=a.pop(-1)
        a.insert(0,x)
        rotation+=1
    Value=-1
    if(I<len(a)):
        Value=a[I]
    return Value
a=[1,2,3,4,5,6,7,8,9,10]
I=5
R=5
print(Index_R_Rotations_Find_I(a,I,R))