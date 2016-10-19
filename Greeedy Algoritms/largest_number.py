#Uses python3
import sys

def largest_number(a):
    #write your code here
    a = [str(i) for i in a]
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i]+a[j] < a[j]+a[i]:
                a[i], a[j] = a[j], a[i]
    return ''.join(a)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
