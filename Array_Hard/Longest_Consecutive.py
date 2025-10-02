
#Brute Force - TC= O(n2) , Sc = O(1)
def longest_sub_seq(arr):
    longest_count=1
    if not arr:
        return 0
    else:
         for elem in arr:
            curr_elem = elem
            cnt =1 
            while linear_search(arr,curr_elem+1):
                curr_elem+=1
                cnt+=1
            longest_count = max(cnt,longest_count)
    return longest_count

def linear_search(arr,search):
    for elem in arr:
        if elem == search:
            return True
    return False

arr = [1, 9, 3, 10, 2, 20, 4]
#print(longest_sub_seq(arr))


#Optimal Approach - TC - O(n), Sc = O(n)
def longest_seq(arr):
    set_arr = set(arr)
    max_count =1 
    for elem in set_arr:
        curr = elem
        if curr-1 not in set_arr:
            start = curr
            cnt = 1
            while(curr+1  in set_arr):
                curr +=1
                cnt+=1
            max_count = max(max_count,cnt)
    return max_count

arr = [1, 9, 3, 10, 2, 20, 4]
print(longest_seq(arr))




#This Solution is wrong- It will not find the correct set
def longest_sub_seq1(arr):
    if not arr:
        return 0
    else:
        longest_arr_count = 1
        curr_count =1 
        for i in range(len(arr)):
            curr = arr[i]
            if curr+1 in arr:
                curr_count+=1
            else:
                longest_arr_count = max(curr_count,longest_arr_count)
                curr_count=1
        return max(curr_count,longest_arr_count)
