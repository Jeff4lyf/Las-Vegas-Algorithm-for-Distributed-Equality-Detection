import random

def gen_subset(m, size):
    return random.sample(range(m), min(size, m))

def fp(s, subset):
    r = 0
    for i in subset:
        r ^= int(s[i])
    return r

def run(U, V, m):
    n = len(U)
    rounds = max(1, m.bit_length())
    cand = list(range(n))

    print("\nINPUT\n")
    for i in range(n):
        print("i =", i, "| U =", U[i], "| V =", V[i])

    print("\n")

    for t in range(1, rounds + 1):
        if not cand:
            break

        size = min(2 ** t, m)
        S = gen_subset(m, size)

        print("Round", t)
        print("S =", S)

        nxt = []

        for k in cand:
            a = fp(U[k], S)
            b = fp(V[k], S)

            if a == b:
                print("k =", k, "|", a, b, "-> keep")
                nxt.append(k)
            else:
                print("k =", k, "|", a, b, "-> drop")

        cand = nxt
        print("now:", cand, "\n")

    print("check\n")

    if not cand:
        print("no match")
        return False

    for k in cand:
        print("k =", k)
        if U[k] == V[k]:
            print("match found")
            return True
        else:
            print("not equal")

    print("no match")
    return False


def test(x):
    m = 8
    n = 10

    print("\ncase", x)

    if x == 1:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V[0] = U[0]

    elif x == 2:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]

    elif x == 3:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = U[:]
        V[4] = format(random.getrandbits(m), f'0{m}b')

    elif x == 4:
        U = ["11110000"] * n
        V = ["11110001"] * n

    else:
        U = ["00000000"] * n
        V = ["11111111"] * n

    run(U, V, m)


for i in range(1, 6):
    test(i)
