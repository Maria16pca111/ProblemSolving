#Left by one Position in array 

def Rotate_Left_one_position(array):
    x=array.pop(0)
    array.append(x)    
    return array
array=[1,2,34,5]

print(Rotate_Left_one_position(array))
