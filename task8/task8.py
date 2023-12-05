import re


def fun(s):
    """возвращает True если адрес корректный,
    иначе возвращает False"""

    if type(s) is not str:
        return

    if re.match('^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$', s) is None:
        return False

    return True


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print(filtered_emails)


if __name__ == '__main__':
    main()
