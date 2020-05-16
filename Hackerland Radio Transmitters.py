import bisect 

def hackerlandRadioTransmittters():
    num = 0
    index = 0;
    for i in range(0,n):
        if(index == n+1):
            break;

        if(index == n-1):
            num += 1
            break;

        if(H[index]+k in H):
            index = bisect.bisect_left(H, H[index]+2*k)+1
            num += 1;
        else:
            index += 1
            num += 1;

    print(num)
# n,k = [int(x) for x in input().split(' ')]
# H = [int(x) for x in set(input().split(' '))]
# H.sort()
n, k = 5,1 
H = [int(x) for x in set('1 2 3 4 5'.split(' '))]
H.sort()
print(H)

hackerlandRadioTransmittters()