# O(n) time complexity
def finder(arr1,arr2):

    if len(arr1) == len(arr2):
        return
    
    numCount = {}
    for num in arr2: # n times
        if num in numCount: # 1 times
            numCount[num] += 1 # 1 time
        else:
            numCount[num] = 1 # 1 time

    for num in arr1: # n times
        if num in numCount and  numCount[num] > 0: # 1 times
            numCount[num] -= 1 # 1 time
        else:
            print("A is larger than B")
            print("{0} is the missing number".format(num)) # time

    #print(numCount)

finder([5,5,7,7],[5,7,7])
