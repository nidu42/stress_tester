from os import system as cmd
from constants import *


while True:
    if create_test_is_py:
        cmd("python {} > test.txt".format(create_test))
    else:
        cmd("./{} > test.txt".format(create_test))

    if prog1_is_py:
        cmd("python {} < test.txt > out1.txt".format(prog1))
    else:
        cmd("./{} < test.txt > out1.txt".format(prog1))

    if prog2_is_py:
        cmd("python {} < test.txt > out2.txt".format(prog2))
    else:
        cmd("./{} < test.txt > out2.txt".format(prog2))

    out1 = open("out1.txt", "r")
    out2 = open("out2.txt", "r")
    s1 = out1.read()
    s2 = out2.read()
    out1.close()
    out2.close()

    if s1 != s2:
        print("FOUND!11!1!!")
        break
