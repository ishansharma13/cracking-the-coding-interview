def palindrome(s):
    i = 0
    j = len(s)-1
    flag = False
    if len(s) == 1:
        return True
    while i < j:
        if s[i] != s[j]:
            flag = False
            break
        else:
            flag = True
            i += 1
            j -= 1

    return flag


def palindromeAfterDeletionOptimised(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == s[j]:
            valid = True
            i += 1
            j -= 1
        else:
            if palindrome(s[i:j]) or palindrome(s[i+1:j+1]):
                valid = True

            else:
                valid = False
            break

    return valid


def palindromeAfterDeletion(s):
    valid = palindrome(s)
    if valid is False:
        for i in range(len(s)):
            tmp = s[:i]+s[i+1:]
            valid = palindrome(tmp)
            if valid is True:
                break
    return valid


def palindromeVer2(s):
    return s == ''.join(reversed(s))


if __name__ == '__main__':
    s = 'a'
    print(palindrome(s))
