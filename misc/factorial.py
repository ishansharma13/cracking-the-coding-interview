def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1

    return x*factorial(x-1)


if __name__ == '__main__':
    x = 5
    print(factorial(x))
