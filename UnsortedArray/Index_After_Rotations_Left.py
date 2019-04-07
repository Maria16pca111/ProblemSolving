#third position after index upto array two rotations left

def Third_Position_Array_Two_Rotation(a):
    count=0
    while(count!=2):
        array=a.pop(-1)
        a.insert(0,array)
        count+=1
        
    count+=1
    return a,array
a=[1,2,3,4,5,6,7,8]
print(Third_Position_Array_Two_Rotation(a))
    