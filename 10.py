election = {}
f = open("input.txt", 'r')

a_set = set((line.strip() for line in open('input.txt')))

for element in a_set:
    election[element] = 0
    election.pop('', None)

for line in f:
    candidate = line.strip()
    try:
        election[candidate] += 1
    except KeyError:
        pass

# Total electorate
a_sum = 0
a_list = []
total = 0

for key in election:
    total += election[key]

votes_max = max(election, key=election.get)
a_list.append(votes_max)
a_sum += (election[votes_max] / total)

election.pop(votes_max, None)

if a_sum <= (1 / 2):
    votes_max = max(election, key=election.get)
    a_list.append(votes_max)
    a_sum += (election[votes_max] / total)

    election.pop(votes_max, None)

for i in a_list:
    print(i)
