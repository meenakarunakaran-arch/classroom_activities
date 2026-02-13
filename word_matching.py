def match_words(words):
    lst = []
    ctr = 0
    for i in words:
        if len(i) > 1 and i[0] == i[-1]:
            ctr += 1
            lst.append(i)
    print(lst)
    return ctr
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])

print("Number of words having first and last character same:", count)