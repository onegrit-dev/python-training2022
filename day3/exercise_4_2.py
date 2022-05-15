f = open('sample.txt', 'w')
lines = ['This', 'is', 'Python', '3']
f.write('\n'.join(lines))
f.close()

# あるいは with文を使って

with open('sample.txt', 'w') as f:
    lines = ['This', 'is', 'Python', '3']
    f.write('\n'.join(lines))
