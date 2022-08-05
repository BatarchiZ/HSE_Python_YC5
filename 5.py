_set = set()
with open('input.txt', 'r') as read_file:
    for line in read_file:
        for word in line.split():
            if word not in _set:
                _set.add(word)

print(len(_set))
