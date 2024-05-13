# Python3 code for the above approach

# function to find the length of longest
# subarray having sum k
def lenOfLongSubarr(arr, N, K):
  
    # Variable to store the answer
    maxlength = 0

    for i in range(0,N):

        # Variable to store sum of subarrays
        Sum = 0

        for j in range(i,N):

            # Storing sum of subarrays
            Sum += arr[j]

            # if Sum equals K
            if (Sum == K):

                # Update maxLength
                maxlength = max(maxlength, j - i + 1)

    # Return the maximum length
    return maxlength

# Driver Code
# Given input
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15

# Function Call
print("Length = " , lenOfLongSubarr(arr, n, k))

# T# Python3 code for the above approach

# function to find the length of longest
# subarray having sum k
def lenOfLongSubarr(arr, N, K):
  
    # Variable to store the answer
    maxlength = 0

    for i in range(0,N):

        # Variable to store sum of subarrays
        Sum = 0

        for j in range(i,N):

            # Storing sum of subarrays
            Sum += arr[j]

            # if Sum equals K
            if (Sum == K):

                # Update maxLength
                maxlength = max(maxlength, j - i + 1)

    # Return the maximum length
    return maxlength

# Driver Code
# Given input
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15

# Function Call
print("Length = " , lenOfLongSubarr(arr, n, k))

# This code is contributed by akashish__

