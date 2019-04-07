def kthSmallest_Array(a):
    a.sort()
    k=input('enter the input')
    return a[k-1]
#a = int(raw_input('Enter how many elements you want: '))
#for i in range(0, a):
 #   x = raw_input('Enter the numbers into the array: ')
a=[4,10,23,12,11]
print(kthSmallest_Array(a))