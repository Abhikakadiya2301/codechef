T = int(input())

def consonant_word(T):
    answer = []
    for i in range(T):
        N = int(input())
        u = input().lower()
        if len(u) <= N:
            S = [u[i:i+4] for i in range(0, len(u), 4)]
            count = 0
            for j in range(len(S)):
                vowels = set('aeiou')
                if S[j] not in vowels:
                    count+=1
        else:
            print(f'Enter word length of {N}')
    for j in range(len(answer)):
        print(answer[j])

consonant_word(T)