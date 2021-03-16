# input section
a = [1,10,9,5,2,8,0]
n = 7

# function
def find_second_lrgst(array, num):
    # sort an array by insertion sort
    for i in range(1,num):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]

    # print out the second largest number located in ahead of the last index
    print(array[num-2])

# execution
find_second_lrgst(a, n)