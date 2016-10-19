# Uses python3
import sys
from collections import namedtuple
from copy import copy

Segment = namedtuple('Segment', 'start end')

def get_2d(segments):
    points = []
    #write your code here
    for s in segments:
        points.append([s.start,s.end])
    return points
u = []
def optimal_points(points_2d):
    right_ends = [i[1] for i in points_2d]
    min_ele = min(right_ends)
    m  = check_func(min_ele,points_2d)
    if len(m) == 0:
        u.append(min_ele)
        return u
    else:
        u.append(min_ele)
        return optimal_points(m)

def check_func(min_element,points_2d):
    a = copy(points_2d)
    for i in points_2d:
        if min_element in range(i[0],i[1]+1):
            a.remove(i)
         #print(i)
    return a
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points_2d = get_2d(segments)
    points = optimal_points(points_2d)
    print(len(points))
    for p in points:
        print(p, end=' ')
