# Uses python3
import sys

def get_change(n):
    #write your code here
    n10 = 0
    m = 0
    n5 = 0
    p = 0

    if n > 0:
        n10 = n//10
        m = n%10
        if m > 0:
           n5 = m//5
           p = m%5

    return int(n10 + n5 + p)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
