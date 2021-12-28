def power(x,n):
    if n == 0:
        return 1
    if x == 1:
        return 1
    return x*power(x,n-1)


if __name__ == '__main__':
    x,n = 1,1000
    print(power(x,n))
