def largestRectangle(H):
    largest_area = 0
    for i in range(1, n+1):
        for j in range(0,n):
            if(j+i>n):
                continue;
            area = i*min(H[j:j+i])
            if(area > largest_area):
                largest_area = area
    print(largest_area)

n = int(input())
H = [int(x) for x in input().split(' ')]
