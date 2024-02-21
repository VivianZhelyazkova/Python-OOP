num = int(input())


def print_upper_part(n):
    for i in range(1, n + 1):
        print(f"{' ' * (n - i)}{'* ' * i}")


def print_bottom_part(n):
    for i in range(n - 1, 0, -1):
        print(f"{' ' * (n - i)}{'* ' * i}")


print_upper_part(num)
print_bottom_part(num)
