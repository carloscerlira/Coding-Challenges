def getLeft(A):
    left = []; left.append(-1);
    not_found = []
    for i in range(1,len(A)):
            left_index = i-1
            for j in range(i-1, -1, -1):
                if (A[left_index] > A[i]):
                    if(left_index == 0):
                        left.append(0)
                    else:
                        left.append(left_index)
                    break;

                if (left[left_index] == -1):
                    left.append(-1)
                    break;
                left_index = left[j]

    return left

def findMaximumIndexProduct(A):
    if(len(A) == 1):
        return 0
    left = getLeft(A)
    left = [x+1 for x in left]

    right = getLeft(A[::-1])[::-1]
    right = [len(A)-x if x != -1 else 0 for x in right]

    print(max(left[i]*right[i] for i in range(1,len(A))))

A = [int(x) for x in '1 1 1 1 0 1 1 1 1 1'.split(' ')]
# n = int(input())
# A = [int(x) for x in input(' ').split()]
findMaximumIndexProduct(A)
