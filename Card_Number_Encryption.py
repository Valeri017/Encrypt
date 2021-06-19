import re

cardRegex = re.compile(r'\d{16}|\d{4} \d{4} \d{4} \d{4}')


def encryption(num):
    """This function takes a bank curd number and replaces all
     numbers with '*' except the last 4"""
    correct_num = cardRegex.search(num)
    if correct_num:
        return print('*' * 12 + num[-4::1])

    else:
        print('incorrect card number')


if __name__ == '__main__':
    encryption('1234123412341234')
    encryption('1234 1234 1234 1234')
