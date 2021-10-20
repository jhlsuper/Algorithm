import random


def insertion_sort():
    print(randint(1, 1000))


def randint(a, b):
    return a + randbelow(b - a + 1)


def randbelow(n):
    if n <= 0:
        return
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r


def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)


insertion_sort()
