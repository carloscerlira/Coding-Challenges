def maxSequence(arr):
    n=len(arr)
    if n == 1:
        return arr[0]
    max_sum = maxSequence(arr[:-1])
    max_sum = max(max_sum, max_sum+arr[-1])
    max_sum = max(max_sum, arr[-1])
    return max_sum

def maxSubarray(arr):
    n=len(arr)
    if n == 1:
        return arr[0]
    max_sum = maxSubarray(arr[:-1])
    for i in range(0, n):
        s = sum(arr[i:n])
        max_sum = max(s, max_sum)
    return max_sum

# t=1
# n=4
# arr=[int(x) for x in '-2 -3 -1 -4 -6'.split(' ')]
# print(theMaximumSubarray(arr))
# print(maxSequence(arr))

t = int(input())

for i in range(t):
    n = int(input())
    arr = [int(x) for x in input().split(' ')]
    print('{} {}'.format(maxSubarray(arr),maxSequence(arr)))


# -1,1,2,3,-100,1,100