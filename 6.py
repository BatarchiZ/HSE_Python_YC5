largest_value = int(input())
a_set = set(map(str, range(1, largest_value + 1)))
line1 = input()
while 'HELP' not in line1:
    line2 = input()
    if 'YES' in line2:
        yes_set = set(line1.split())
        a_set &= yes_set
    else:
        no_set = set(line1.split())
        a_set -= no_set
    line1 = input()
print(*sorted(a_set))
