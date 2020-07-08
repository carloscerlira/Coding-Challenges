def sums(string):
    s = 0
    k = 1
    for i in range(len(string)-1,-1,-1):
        s += int(string[i])*(i+1)%(1e9+7)*k%(1e9+7)
        k = (k*10+1)%(1e9+7)
    return int(s%(1e9+7))
string = input()
print(sums(string))
