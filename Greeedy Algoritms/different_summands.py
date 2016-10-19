# Uses python3
import sys

def optimal_summands(n):
    total = 0
    increment = 1
    count = 0
    a = []

    while total + increment <= n:
        total += increment
        a.append(increment)
        increment += 1
        count += 1

    a[count-1] += n - total

    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
