# array reverse order

def reverse_order_array(array):
        b=[]
        for x in range(array[-1],array[0],-1):
                b.append(x)
        print(b)

array=[1,2,3,4,5]
reverse_order_array(array)
