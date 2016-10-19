# Uses python3
import sys

# def fibonacci_partial_sum_naive(from_, to):
#     if to <= 1:
#         return to
#
#     previous = 0
#     current  = 1
#
#     for _ in range(from_ - 1):
#         previous, current = current, previous + current
#
#     sum = current
#
#     for _ in range(to - from_):
#         previous, current = current, previous + current
#         sum += current
#
#     return sum % 10
def calc_fib(n,m):
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]

def fibonacci_huge(n,m):
    if n < m:
        return calc_fib(n,m)
    new_n = n % (6 * m)
    return calc_fib(new_n,m)

def partial_sum(n,m):
    return ((fibonacci_huge(m+2,10)) - (fibonacci_huge(n+1,10)))%10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(partial_sum(from_, to))
