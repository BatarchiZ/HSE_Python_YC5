largest_value = int(input())
numbers = set(range(1, largest_value + 1))
while True:
    line1 = input()
    if 'HELP' in line1: break
    guess = set(map(int, line1.split()))
    if len(guess & numbers) <= len(numbers) / 2:
        print('NO')
        numbers -= guess
    else:
        print("YES")
        numbers &= guess

print(*sorted(numbers))
