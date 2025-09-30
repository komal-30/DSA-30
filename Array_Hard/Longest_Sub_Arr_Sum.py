def longest_subarray_sum(arr,k):
    max_sum=0
    max_sum_arr =[]
    max_sub_arr_len=0
    for ind in range(len(arr)-1):
        sum_arr = 0
        for ind1 in range(ind,len(arr)):
            sum_arr = arr[ind]+ arr[ind1]
            if sum_arr==k:
                max_sum_arr.append(arr[ind],arr[ind1])
                max_sub_arr_len = len(max_sum_arr)

                

            
 {2,3,5,1,9}