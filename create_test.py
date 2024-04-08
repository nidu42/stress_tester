from random import randint

t = randint(1, int(1e4))
test_file = open("test.txt", "w")
test_file.write("{}\n".format(t))
for _ in range(t):
    n = randint(1, int(2e5) // t)
    k = randint(1, int(1e15))
    a = [randint(1, int(1e9)) for _ in range(n)]
    test_file.write("{} {}\n".format(n, k))
    test_file.write(("{} " * n + "\n").format(*a))
test_file.close()
