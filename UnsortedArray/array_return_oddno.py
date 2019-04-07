#display the odd numbers in an array
def oddno_array(arr):
    for x in arr:
        if not(x%2==0):
            print(x)
arr=[1,3,4,5,5,7,2,10]
print(oddno_array(arr))