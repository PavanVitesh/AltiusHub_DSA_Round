# Rotate array by K positions

def rotate_array(arr,k): # rotating array by k elements
    return arr[k:]+arr[:k] # slicing array from kth inex till last and then add the 1st k elemets at the end

# Time Complexity : O(1)
# Space Complexity : O(1)

