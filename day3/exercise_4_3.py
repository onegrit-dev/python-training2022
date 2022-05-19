lines = ['I', 'like', 'Python']

with open('sample2.txt', 'w') as f:
    f.writelines(' '.join(lines))
