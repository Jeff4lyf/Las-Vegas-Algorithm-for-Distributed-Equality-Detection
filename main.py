import random

def generate_random_subset(m, size):
    return random.sample(range(m), min(size, m))

def fingerprint(string, subset):
    res = 0
    for i in subset:
        res ^= int(string[i])
    return res

def las_vegas_match(U, V, m):
    n = len(U)
    r = int(2 * (m.bit_length()))  # O(log m)

    candidates = list(range(n))

    for t in range(1, r + 1):
        new_candidates = []
        subset_size = min(2 ** t, m)

        for k in candidates:
            S = generate_random_subset(m, subset_size)

            fu = fingerprint(U[k], S)
            fv = fingerprint(V[k], S)

            if fu == fv:
                new_candidates.append(k)

        candidates = new_candidates

        if not candidates:
            return False

    for k in candidates:
        if U[k] == V[k]:
            return True

    return False


m = 32
U = [format(random.getrandbits(m), f'0{m}b') for _ in range(10)]
V = U.copy()


V[3] = format(random.getrandbits(m), f'0{m}b')

print("Match exists:", las_vegas_match(U, V, m))
