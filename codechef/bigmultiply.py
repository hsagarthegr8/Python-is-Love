import numpy as np

def solution():
    for t in range(int(input())):
        m,n = [x for x in input().split()]
        m = np.array([int(x) for x in m])
        n = np.array([int(x) for x in n])
        print((m.sum() % 3 * n.sum() %3)%3)


if __name__ == '__main__':
    solution()