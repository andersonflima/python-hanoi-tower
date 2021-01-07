def move(x, y):
    print(f"Move disc from {x} to {y}!")


def hanoi(n=4, a="A", b="B", c="C"):
    if n == 0:
        return
    hanoi(n - 1, a, c, b)
    move(a, c)
    hanoi(n - 1, b, a, c)


if __name__ == "__main__":
    hanoi()