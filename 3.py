a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

intersection_set = a_set & b_set

a_list = list(intersection_set)

ordered_list = sorted(a_list)
print(*ordered_list, end=' ')
