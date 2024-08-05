# Maximum sub array problem using kandens algorithm

def max_sum_sub_array(arr):
    res = -1*float("inf") # considering this to be actual result since we need maximum value initializing with possible minimum value 
    temp = 0 # a temporary variable to store intermediate result
    for i in arr:
        temp+=i # adding current value of array to temp variable
        res = max(res,temp) # updating result wit maximum value of overall result to temporary result
        if temp < 0: # if intemediate result goes to negative values changing that with current value
            temp = i
    return res 

# Time Complexity : O(n) where n is length of the Array because we are iterating through the array in 1 single loop
# Space Complexity : O(1) because every time we are taking extra space of only 2 variables not depending on n so order of 1
