
def majority_elem(arr): 
    maj = arr[0]
    count=0
    for elem in arr:
        if elem == maj:
            count+=1
        else:
            count-=1
        if count == 0:
            maj = elem
            count=1
    
    #Checking
    cnt1 = 0
    for i in range(len(arr)):
        if arr[i] == maj:
            cnt1 += 1
    if cnt1 > (len(arr) /3 ):
        return maj
    return -1
    

arr =  [11,33,33,11,33,11]
print(majority_elem(arr))

