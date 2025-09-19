def rearrange_by_sign(arr):
    pos_arr =[]
    neg_arr =[]
    final_arr=[]
    for elem in arr:
        if elem >0:
            pos_arr.append(elem)
        else:
            neg_arr.append(elem)

    #even -> pos
    #odd-> neg
    for i in range(len(pos_arr)):
        arr[2*i] = pos_arr[i]

    for i in range(len(neg_arr)):
        arr[2*i+1] = neg_arr[i]
        
        
    