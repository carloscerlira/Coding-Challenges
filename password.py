import numpy as np 

def getStrength(password, w_a):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    keys = [letter for letter in alphabet]
    values = [(w_a+i)%26 for i in range(0,27)]
    dic = dict(zip(keys, values))
    
    strenght = 0
    for letter in password:
        strenght += dic[letter]

    print(strenght)

getStrength('mzbmweyydiadtlcouegmdbyfwurpwbpuvhifnuapwyndmhtqvkgkbhtytszotwflegsjzzszfwtzfpnscguemwrczqxycivdqnky', 15)
# password, w_a = input().split(' ')
# w_a = int(w_a)
# print(password, w_a)