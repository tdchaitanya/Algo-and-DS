# Uses python3
import sys

def calc_fib(n,m):
    fibs = [0,1]
    for i in range(2,n+1):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[n]%m

def pisano_period(n,m):
    if m%10 in [10,100,1000,10000,100000,1000000]:
        return 6*m
    fibs = [0,1]
    fibs_modded = [0,1]
    k = 0
    for i in range(2,n+1):
        fibs.append((fibs[-1]%m + fibs[-2]%m)%m)
        fibs_modded.append(fibs[-1]%m )
        k += 1
        if k >= 3 :
            if fibs_modded[-1] == 1 :
                if fibs_modded[-2] == 0:
                    return len(fibs_modded)-2
    return m

def fibonacci_huge(n,m):
    if n < m:
        return calc_fib(n,m)
    period_length = pisano_period(n,m)
    new_n = n % period_length
    return calc_fib(new_n,m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_huge(n, m))
