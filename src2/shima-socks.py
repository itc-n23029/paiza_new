a, b = int(input()), int(input())


def f(a, b):
    return "".join(["R" if (i // a) % 2 == 0 else "W" for i in range(b)])


result = f(a, b)
print(result)
