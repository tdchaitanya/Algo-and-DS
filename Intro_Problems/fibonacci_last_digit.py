# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-1]%10 + fibs[-2]%10)

    # if n <= 1:
    #     return n
    #
    # previous = 0
    # current  = 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #
    return fibs[n]%10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
