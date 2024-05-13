import sys


def lenOfLongSubarr(A, N, K):
    sum_index_map = {0: -1}  # Dictionary to store cumulative sum and its index
    maxLen = 0
    prefix_sum = 0

    for i in range(N):
        prefix_sum += A[i]
        
        #no need to this case bease we are stroing the sum 0 with index -1 initially
        #if prefix_sum==k:
        #  maxLen=i+1
        
        
        # If prefix_sum-K is found in the map, update maxLen
        if prefix_sum - K in sum_index_map:
            length = i - sum_index_map[prefix_sum - K]
            maxLen = max(maxLen, length)

        # Store the index of the cumulative sum if it's not already in the map
        if prefix_sum not in sum_index_map:
            sum_index_map[prefix_sum] = i

    return maxLen


# Driver Code
arr = [10, 5, 2, 7, 1, 9]
n = len(arr)
k = 15
print("Length = " + str(lenOfLongSubarr(arr, n, k)))
