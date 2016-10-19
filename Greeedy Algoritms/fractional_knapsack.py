# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	capacity = float(capacity)
	total = 0.0
	vals = []
	for i in range(len(weights)):
		vals.append([float(values[i]/weights[i]),weights[i],values[i]])
	m = sorted(vals,key = lambda x:-x[0])
	for p in m :
		while capacity >= 0.0 and p[1] > 0 :

			p[1] -= 1
			if capacity <= 0:
				break
			capacity -=	1
			total += p[0]
	return total

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
