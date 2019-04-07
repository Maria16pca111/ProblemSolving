#a subset of A of size two that adds upto X and print the values that adds upto X.

def subset_adds_values(a,A,x):    
    for i in a:
        for j in A:
            if i+j==x:
                print(i,j)
a=[1,2,3,4,5]
A=[15,3,2]
x=20
print(subset_adds_values(a,A,x))

#notes:
#sum function does not applied due to error results
