f = open("input.txt", 'r')
number_of_words = int(f.readline())

a_dict = {}
while number_of_words != 0:
    a_line = list(map(str, f.readline().split()))
    a_dict[a_line[1]] = a_line[0]

    number_of_words -= 1
i = f.readline().strip()

try:
    print(a_dict[i])
except KeyError:
    b_dict = {value: key for key, value in a_dict.items()}
    print(b_dict[i])
