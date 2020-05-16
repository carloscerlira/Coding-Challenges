import numpy as np 

w_s = input()
n = int(input())

for i in range(n):
    one_s, one_n, two_s, two_n = input().split(' ');
    one_n = int(one_n); two_n = int(two_n)
    if(one_s == w_s and two_s != w_s):
        print('Player one wins')
        continue;
    if(two_s == w_s and one_s != w_s):
        print('Player two wins')
        continue;
    if(one_n == two_n):
        print('Draw')
        continue;
    if(one_n > two_n):
        print('Player one wins')
        continue;
    else:
        print('Player two wins')
        continue;
    