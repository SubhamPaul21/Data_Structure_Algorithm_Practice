# O(n) time complexity
def anagram(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    charCounter = {}

    if len(s1) != len(s2): # 1 time
        return False
    
    for char in s1: # n times
        if charCounter in char: # 1 time
            charCounter[char] += 1 # 1 time
        else:
            charCounter[char] = 1 # 1 time
    
    for char in s2: # n times
        if charCounter in char: # 1 time
            charCounter[char] -= 1 # 1 time
        else:
            charCounter[char] = 1 # 1 time
    
    for value in charCounter.values(): # n times
        if value != 0: # 1 time
            return False
    
    return True

print(anagram('aabbcc','aabbc'))