def can_use_language(A, B, A1, B1, A2, B2):
    if (A == A1 and B == B1) or (A == B1 and B == A1):
        return 1
    elif (A == A2 and B == B2) or (A == B2 and B == A2):
        return 2
    else:
        return 0

# Sample Input
T = int(input())
for i in range(T):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    print(can_use_language(A, B, A1, B1, A2, B2))
