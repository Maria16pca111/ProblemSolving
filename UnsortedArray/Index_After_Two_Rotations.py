#third position after index upto array two rotations

def Third_Position_Array_Two_Rotation(a):
    count=0
    while(count!=2):
        array=a.pop(0)
        count+=1
        a.append(array)
    count+=1
    return a,array
a=[1,2,3,4,5,6,7,8]
print(Third_Position_Array_Two_Rotation(a))
    

