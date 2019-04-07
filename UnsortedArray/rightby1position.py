#return the contents of the array rotate by right one position

def Rotate_Right_one_position(array):
    x=array.pop(-1)
    array.insert(0,x)
    return array
array=[1,2,34,5]
print(Rotate_Right_one_position(array))
    
        