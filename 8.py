dict_lines = int(input())
dict_set = set()
dict_set_lower = set()
while dict_lines != 0:
    LOLOLOLOS = input()
    dict_set.add(LOLOLOLOS)
    dict_set_lower.add(LOLOLOLOS.lower())
    dict_lines -= 1

kolya_salam = list(input().split())
kolya_salam_correct = list()

for i in dict_set:
    try:
        kolya_salam.remove(i)
    except ValueError:
        break
counter_wrong = 0

for word in kolya_salam:
    counter = 0
    for letter in word:
        if letter.isupper():
            counter += 1
        if counter > 1:
            counter = 0
            break
    if counter == 1:

        counter = 0
        if word.lower() in dict_set_lower and word not in dict_set:
            pass
        else:
            kolya_salam_correct.append(word)

print(len(kolya_salam) - len(kolya_salam_correct))
