test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("The original dictionary is :"+str(test_dict))
k = 2
r = 0
for i in test_dict:
    if test_dict[i] == k:
        r = r+1
print("frequncy of k is",r)
