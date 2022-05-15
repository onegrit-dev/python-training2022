f = open('sample.txt')
for line in f:
    print(line)
f.close()

# あるいは with文を使って

with open('sample.txt') as f:
    for line in f:
        print(line)
