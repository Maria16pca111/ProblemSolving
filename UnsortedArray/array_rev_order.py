#print the contents of the array of reverse in order

# def Array_Reverse_Order(arr):
#     b=[]
#     x=arr[-1]
#     y=arr[0]
#     for z in range(x,y,-1):
#         b.append(z)
#     print(b)
# arr=[1,2,3,4,5]
# Array_Reverse_Order(arr)

def reverse(a):
    x=a[::-1]
    print(x)
a=[1,3,5,6,7,8]
reverse(a)