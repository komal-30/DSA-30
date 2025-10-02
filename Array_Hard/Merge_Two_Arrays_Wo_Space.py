#Brute Force
#This solution is not exactly the same.
'''
Time Complexity: O(n+m) + O(n+m), where n and m are the sizes of the given arrays.
Reason: O(n+m) is for copying the elements from arr1[] and arr2[] to arr3[]. And another O(n+m) is for filling back the two given arrays from arr3[].

Space Complexity: O(n+m) as we use an extra array of size n+m.
'''
def merge_array(arr1,arr2):
    arr_pointer1 =0
    arr_pointer2=0
    arr_len1 = len(arr1)
    arr_len2 = len(arr2)
    #Important step , if you do a=[], it will give you index error while first insertion at line 14 
    arr3 = [0] * (arr_len1 + arr_len2)
    arr3_ind=0


    while arr_pointer1<arr_len1 and arr_pointer2 < arr_len2:
        if arr1[arr_pointer1] <= arr2[arr_pointer2]:
            arr3[arr3_ind] = arr1[arr_pointer1]
            arr3_ind+=1
            arr_pointer1+=1
        else:
            arr3[arr3_ind] = arr2[arr_pointer2]
            arr3_ind+=1
            arr_pointer2+=1

    while arr_pointer1 < arr_len1:
        arr3[arr3_ind] = arr1[arr_pointer1]
        arr_pointer1+=1
        arr3_ind+=1
        

    while arr_pointer2 < arr_len2:
        arr3[arr3_ind] = arr2[arr_pointer2]
        arr_pointer2+=1
        arr3_ind+=1
    
    arr1 = arr3[0:arr_len1] 
    arr2 = arr3[arr_len1:]

    return arr1,arr2
arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
#print(merge_array(arr1,arr2))

#OPtimal Solution 1
'''
Time Complexity: O(min(n, m)) + O(n*logn) + O(m*logm), where n and m are the sizes of the given arrays.
Reason: O(min(n, m)) is for swapping the array elements. And O(n*logn) and O(m*logm) are for sorting the two arrays.

Space Complexity: O(1) as we are not using any extra space.
'''

def merge_array1(arr1,arr2):
    n=len(arr1)
    m = len(arr2)
    left=n-1
    right=0
    while left>=0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left],arr2[right] =  arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    arr1.sort()
    arr2.sort()

    return arr1,arr2

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
print(merge_array1(arr1,arr2))



