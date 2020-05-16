import numpy as np 

def maximum(data):
    max_heads = 0; max_tails = 0
    for i in range(0, len(data)):
        if (data[i] == 'Heads'):
            local_max = 1
            for j in range(i+1, len(data)):
                if (data[j] == 'Heads'):
                    local_max += 1;
                if (data[j] == 'Tails'):
                    i = j-1;
                    break;
            if(local_max > max_heads):
                max_heads = local_max
            continue;

        if (data[i] == 'Tails'):
            local_max = 1
            for j in range(i+1, len(data)):
                if (data[j] == 'Tails'):
                    local_max += 1;
                if (data[j] == 'Heads'):
                    i = j-1;
                    break;
            if(local_max > max_tails):
                max_tails = local_max
            continue;
    print(max_heads, max_tails)

n = int(input())
data = []
for i in range(0, n):
    data.append(input())
print(data)
maximum(data)