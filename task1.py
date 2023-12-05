def is_prime(n):
    if not isinstance(n, int) or n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def my_test_is_prime():
    test_cases = (
        ('not a number', False),
        (-1, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (6, False),
        (7, True),
        (9, False),
        (16, False),
    )
    for in_n, correct_answer in test_cases:
        answer = is_prime(in_n)
        #print(answer, correct_answer)
        if correct_answer != answer:
            return False
    return True


print('YES') if my_test_is_prime() else print('NO')
