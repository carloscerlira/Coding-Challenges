def first(n):
    s = 0;
    for i in range(1,n+1):
        s += i;
    return s;

def sherlockAndAnagrams(S):
    L = [x for x in set(S)]
    num = 0
    for i in range(1,len(S)):
        counts = []
        for j in range(0, len(S)):
            if(j+i>len(S)):
                break;
            counts.append(tuple([S[j:j+i].count(l) for l in L]))
        counts = tuple(counts)
        counts = [counts.count(x) for x in set(counts)]
        counts = [first(x-1) if x>=2 else 0 for x in counts]
        num += sum(counts)
    print(num)

k = int(input())
for case in range(0, k):
    S = input()
    sherlockAndAnagrams(S)