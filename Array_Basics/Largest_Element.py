'''Handles all edges cases -> TC = o(n) SC= o(1)'''

def largest_element(list_arr):
    if not list_arr:
        return None
    else:
        max = list_arr[0]
        for num in list_arr:
            if num > max:
                max = num
        return max

''' Works all edge cases -> TC = o(n) SC= o(1) '''

def largest_element3(list_arr):
    return max(list_arr) if list_arr else None

''' This solution wont work for following cases: Empty array,array <=2 elements
TC = o(n) SC= o(1) '''

def largest_element1(list_arr):
    max_number = float('-inf')
    for index in range(0,len(list_arr)-2):
        start_number = list_arr[index]
        next_number = list_arr[index+1]
        if(start_number>next_number and start_number > max_number):
            max_number = start_number
        elif(next_number > max_number): 
            max_number = next_number
    return max_number

'''
This solution wont work for following cases:
Empty array, add ternary condition
TC = o(nlogn) SC= o(n)
Sorting creates a new list copy in Python → O(n)

'''

def largest_element2(list_arr):
    return sorted(list_arr)[-1]

def largest_element2_1(list_arr):
    return sorted(list_arr)[-1] if list_arr else None



list_arr = []
print(largest_element2_1(list_arr))





   


