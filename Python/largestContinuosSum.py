def large_cont_sum(arr):

    if len(arr) == 0: # 1 time
        print("Empty array")
    elif len(arr) == 1: # 1 time
        print(arr[0])
    else:
        sum = 0
        largestSum = 0
        for i in range(len(arr)): # n times
            j = i
            sum = 0 
            while j < len(arr): 
                #print(arr[j])
                sum += arr[j]
                if sum > largestSum and largestSum != sum:
                    largestSum = sum
                j += 1

    # for num in arr:
    #     if num >= 0:
    #         sum += num
    #     else:
    #         if sum > largestSum:
    #             largestSum = sum
    #         sum = 0
    
    print(largestSum)



large_cont_sum([-1,1])