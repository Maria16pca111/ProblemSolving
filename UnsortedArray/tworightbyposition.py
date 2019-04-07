# return the array contents after rotating right two position

def Rotate_Right_Two_position(array):
    count=0
    for x in array:
        x=array.pop(-1)
        array.insert(0,x)
        count+=1
        if(count==2):
            break
    return array
array=[1,2,34,5]
print(Rotate_Right_Two_position(array))
    