def longest_consecutive_seq(nums):
    num_set = set(nums)
    longest_streak = 1
    for num in num_set:
        if num-1 not in num_set:
            count=1
            curr = num
            while curr+1 in num_set:
                curr+=1
                count+=1
            longest_streak= max(longest_streak,count)
    return longest_streak

nums = [100, 200, 1, 2, 3, 4]
print(longest_consecutive_seq(nums))










   


   

arr =  [3, 8, 5, 7, 6]
print(longest_consecutive_seq(arr))

