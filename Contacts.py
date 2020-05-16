import bisect 
A = []
n = int(input())
for i in range(0,n):
    operation, name = input().split(' ')
    if(operation == 'add'):
        bisect.insort(A, name)
    if(operation == 'find'):
        num = 0
        start = bisect.bisect(A, name)
        if(start-1 != -1 and A[start-1] == name):
            num += 1
        for i in range(start, len(A)):
            if (A[i][:len(name)] == name):
                num +=1 
            else:
                break;
        print(num)
