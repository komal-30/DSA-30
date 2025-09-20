def kadane_algo(arr):
    max_sum = float('-inf')
    curr_sum = 0
    start = end = temp_start = 0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        if(max_sum<curr_sum):
            max_sum=curr_sum
            start = temp_start
            end = i

        if curr_sum<0:
            curr_sum=0
            temp_start = i + 1 

    return arr[start:end+1]


arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(kadane_algo(arr))