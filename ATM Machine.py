
def ATM(N,K,A):
    amount = K
    output = []
    for i in range(len(A)):
        if A[i] <= amount:
            amount -= A[i]
            output.append(1)
        else:
            output.append(0)
    return output
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if len(A) == N:
        pass
    else:
        print(f"Enter {N} numbers")
    result = ATM(N, K, A)
    print(''.join(map(str, result)))


