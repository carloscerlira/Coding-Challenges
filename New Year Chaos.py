def minimumBribes(q):
    bribes = 0
    last = len(q);
    for i in range(0, len(q)):
        start_pos = q[::-1][i]
        if (start_pos != max(q[:last])):
            num=1
            for j in range(i+1, len(q[:last])):
                if(q[::-1][j]<q[::-1][j+1]):
                    num += 1
                else:
                    break;
            print(num)
            bribes += num
            last -= 1
        else:
            continue;
    print(bribes)        

q = [int(x) for x in '45312']
# for i in range(0,len(q)):
#     print(q[::-1][i])
#     print(q[i])
    
# print(max(q[:len(q)]))
minimumBribes(q)

# N = int(input())

# for n in range(N):
#     q_size = int(input())
#     q = [int(x) for x in input().split(' ')]
#     minimumBribes(q)

