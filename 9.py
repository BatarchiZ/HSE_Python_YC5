bank = {}
f = open("input.txt", 'r')
for line in f:
    phrase = line.split()
    if phrase[0] == "DEPOSIT":
        try:
            bank[phrase[1]] += int(phrase[2])
        except KeyError:
            bank[phrase[1]] = int(phrase[2])
    elif phrase[0] == "WITHDRAW":
        try:
            bank[phrase[1]] -= int(phrase[2])
        except KeyError:
            bank[phrase[1]] = -int(phrase[2])
    elif phrase[0] == "TRANSFER":
        if phrase[1] not in bank:
            bank[phrase[1]] = 0
        if phrase[2] not in bank:
            bank[phrase[2]] = 0
        bank[phrase[1]] -= int(phrase[3])
        bank[phrase[2]] += int(phrase[3])
    elif phrase[0] == "INCOME":
        for account in bank.keys():
            if bank[account] > 0:
                bank[account] *= (1 + (int(phrase[1]) / 100))
                bank[account] = int(bank[account])
    else:
        if phrase[1] not in bank:
            print("ERROR")
        else:
            print(bank[phrase[1]])
f.close()
