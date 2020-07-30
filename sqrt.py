from sys import argv
def sqrt(n, r):
    return 0.5 * (r + n/r)

def rpt(n):
    prev = sqrt(n, 1)
    curr = sqrt(n, prev)
    while prev != curr:
        prev, curr = curr, sqrt(n, curr)
    return '{0:.2f}'.format(curr)
print(rpt(int(argv[1])))
