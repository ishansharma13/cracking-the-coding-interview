import string


def excelSheetColumnNumber(s):
    letters = [x for x in string.ascii_uppercase]
    numbers = list(range(1, 27))
    mappings = dict(zip(letters, numbers))
    res = 0

    for i in range(len(s)-1, -1, -1):
        mult = 26**(len(s)-i-1)
        res += (mult*mappings[s[i]])

    return res


if __name__ == '__main__':
    s = 'ZY'
    print(excelSheetColumnNumber(s))
