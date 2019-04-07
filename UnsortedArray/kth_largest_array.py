# find the elements in array by considering the kth largest

def kth_largest(a):
    a.sort()
    k=int(input('enter element k'))
    return(a[-k])
a=[1,2,3,4,8,7,9,10,11,6]
print(kth_largest(a))