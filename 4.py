numbers = tuple(map(int, input().split()))
_set = set()
for number in numbers:
    if number not in _set:
        _set.add(number)
        print('NO')
    else:
        print('YES')
