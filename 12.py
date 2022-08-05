f = open("input.txt", 'r')
a_dict = {}
for line in f:
    for word in line.split():
        try:
            a_dict[word] += 1
            print(a_dict[word])
        except KeyError:
            a_dict[word] = 0
            print(a_dict[word])
