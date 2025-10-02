def majority_element(arr):
    me1 = float('-inf')
    me2 = float('-inf')
    c1 =0
    c2 = 0

    for curr_elem in arr:
        if c1==0 and curr_elem !=me2:
            c1=1
            me1=curr_elem
        elif  c2==0 and curr_elem !=me1:
            c2=1
            me2=curr_elem
        elif me1 == curr_elem:
            c1+=1
        elif  me2 == curr_elem:
            c2+=1
        else:
            c1-=1
            c2-=1

    ls = [] # list of answers

    # Manually check if the stored elements in
    # el1 and el2 are the majority elements:
    cnt1, cnt2 = 0, 0
    for i in range((len(arr))):
        if arr[i] == me1:
            cnt1 += 1
        if arr[i] == me2:
            cnt2 += 1

    mini = int(len(arr) / 3) + 1
    if cnt1 >= mini:
        ls.append(me1)
    if cnt2 >= mini:
        ls.append(me2)

    return ls


arr = [11, 33, 33, 11, 33, 11]
print(majority_element(arr))
            