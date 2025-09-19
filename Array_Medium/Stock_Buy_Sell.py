def stock_buy_sell(arr):
   min_num = min(arr)
   min_ind = arr.index(min_num)
   max_num = max(arr[min_ind:])
   if max_num:
        return max_num-min_num
   return None

arr =  [7,1,5,3,6,4]
print(stock_buy_sell(arr))
