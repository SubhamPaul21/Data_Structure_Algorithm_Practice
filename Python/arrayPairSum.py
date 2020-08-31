# O(n) time complexity
def pair_sum(arrayList, amount):

    if len(arrayList) < 2: # 1 time
        return

    seen = set()
    output = set()

    for num in arrayList: # n times
        target = amount - num

        if target in seen: # 1 time
            output.add( (min(num, target), max(num, target)) )
        else:
            seen.add(num)
    
    print(output)
    
pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)


# O(n^2) time complexity
# counter = 0
# for i in range(len(arrayList)): # n times
#     for j in range(i+1, len(arrayList)): # m times
#         if arrayList[i] + arrayList[j] == sum:
#             counter += 1
#             print("(" + str(arrayList[i]) + "," + str(arrayList[j]) + ")")

# print(counter)