def SherlockAndTheValidString(word):
    times = []
    for letter in set(word):
        times.append(word.count(letter))
    
    print(times)
    most_common = max([times.count(x) for x in set(times)])
    least_common = min([times.count(x) for x in set(times)])
    print(most_common, least_common)
word = 'aaaabbcc'
print(SherlockAndTheValidString(word))