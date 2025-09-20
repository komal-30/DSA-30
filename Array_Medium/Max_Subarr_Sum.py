#Brute Force Approach - O(n2)
def max_subarr_sum(arr):
    n = len(arr)
    max_sum = float('-inf')
    max_subarr = []

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_subarr = arr[i:j+1]
    
    return max_sum, max_subarr

#Kadane's Algorithm - O(n)
def max_sum(arr):
    curr_sum = arr[0]
    max_sum = arr[0]
    for elem in range(1,len(arr)):
        curr_sum += arr[elem]
        if max_sum>curr_sum:
            max_sum=curr_sum
        if curr_sum<0:
            curr_sum=0
    return max_sum
            

class KadaneAlgorithm:
    def max_sub_array(self, nums):
        current_sum = nums[0]   # sum of subarray ending at current index
        max_sum = nums[0]       # best sum found so far

        for i in range(1, len(nums)):
            # Step 1: Decide whether to extend or start new
            current_sum = max(nums[i], current_sum + nums[i])

            # Step 2: Update global maximum
            max_sum = max(max_sum, current_sum)
        
        return max_sum

    
   
[-2,1,-3,4,-1,2,1,-5,4] 

-2+1=-1