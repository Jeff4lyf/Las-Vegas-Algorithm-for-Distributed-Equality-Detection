import random

def generate_subset(m, size):
    return random.sample(range(m), min(size, m))

def fingerprint(binary_string, subset):
    result = 0
    for i in subset:
        result ^= int(binary_string[i])
    return result

def las_vegas_equality(U, V, m):
    n = len(U)
    rounds = max(1, m.bit_length())  # ~log m

    candidates = list(range(n))

    print("\n========== INPUT ==========")
    for i in range(n):
        print(f"Index {i}: U = {U[i]} | V = {V[i]}")
    print("===========================\n")

    for t in range(1, rounds + 1):
        if not candidates:
            break

        subset_size = min(2 ** t, m)
        subset = generate_subset(m, subset_size)

        print(f"--- Round {t} ---")
        print(f"Subset size: {subset_size}")
        print(f"Subset indices: {subset}")

        new_candidates = []

        for k in candidates:
            fu = fingerprint(U[k], subset)
            fv = fingerprint(V[k], subset)

            status = "KEEP" if fu == fv else "REMOVE"
            print(f"Index {k}: f(U)={fu}, f(V)={fv} → {status}")

            if fu == fv:
                new_candidates.append(k)

        candidates = new_candidates
        print(f"Remaining candidates: {candidates}\n")

    # Final verification
    print("===== FINAL VERIFICATION =====")

    if not candidates:
        print("No candidates remaining.")
        print("\nOutput: Match exists = False")
        return False

    for k in candidates:
        print(f"Comparing index {k}...")
        if U[k] == V[k]:
            print(f"Index {k}: EXACT MATCH FOUND")
            print("\nOutput: Match exists = True")
            return True
        else:
            print(f"Index {k}: Not equal")

    print("\nOutput: Match exists = False")
    return False


# ====== TEST CASES ======

def run_test_case(case_num):
    m = 8
    n = 10

    print(f"\n\n========== TEST CASE {case_num} ==========")

    # Case 1: One match
    if case_num == 1:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V[0] = U[0]  # force match

    # Case 2: No match
    elif case_num == 2:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]

    # Case 3: Multiple matches
    elif case_num == 3:
        U = [format(random.getrandbits(m), f'0{m}b') for _ in range(n)]
        V = U.copy()
        V[3] = format(random.getrandbits(m), f'0{m}b')  # break one

    # Case 4: Late elimination
    elif case_num == 4:
        U = ["11110000"] * n
        V = ["11110001"] * n  # very similar

    # Case 5: Immediate elimination
    else:
        U = ["00000000"] * n
        V = ["11111111"] * n

    las_vegas_equality(U, V, m)


# Run all test cases
for i in range(1, 6):
    run_test_case(i)
