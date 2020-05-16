def BiggerIsGreater(word):
    word = word[::-1]
    index = 0;
    for i in range(1,len(word)):
        for j in range(0,i):
            if(word[i]<word[j]):
                word[i], word[j] = word[j], word[i]
                index = len(word)-i
                break;
        else:
            continue;
        break;
    word = word[::-1]
    
    for i in range(index, len(word)):
        for j in range(i, len(word)):
            if (word[i]>word[j]):
                word[i], word[j] = word[j], word[i]

    if(index == 0):
        return ('no answer')

    else:
        return ''.join(word)        

N = int(input())
for n in range(0,N):
    print(BiggerIsGreater([x for x in input()]))
