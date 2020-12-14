from sympy import Matrix
from diophantine import solve

with open("d13p2.txt") as f:
    s = f.readlines()[1]
    l = [int(x) if x != "x" else None for x in s.split(",")]
    ls = [x for x in l if x is not None]

    m = []
    for i, x in enumerate(ls):
        if x:
            r = [0]*len(ls)
            r[i] = x
            r.append(-1)
            m.append(r)

    A = Matrix(m)
    b = [i for i, x in enumerate(l) if x]
    X = solve(A, b)
    print(X[0][-1])
