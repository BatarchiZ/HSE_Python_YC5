a_dict = {}
f = open("input.txt")
Countries_N = int(f.readline())
stopN = 0

# Making Dict
while Countries_N > stopN:
    line = f.readline().split()
    key = line[0]
    value_list = line[1::]
    for city in value_list:
        a_dict[city] = key

    stopN += 1

stopN = 0
Countries_N = int(f.readline())
while Countries_N > stopN:
    key = f.readline().split()[0]
    try:
        print(a_dict[key])
    except KeyError:
        print(0)
    stopN += 1
