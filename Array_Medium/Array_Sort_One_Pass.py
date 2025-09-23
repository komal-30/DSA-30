#TC = n+n = 2n
#SC = O(1)
def sort_arr(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)
    
    for i in range(count_0):
        arr[i] = 0
    for i in range(count_0,count_0+count_1):
        arr[i] = 1
    for i in range(count_0+count_1,len(arr)):
        arr[i] = 2

    return arr
    

arr = [2,0,2,1,1,0]
print(sort_arr(arr))
            


            