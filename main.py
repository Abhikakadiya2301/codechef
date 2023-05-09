t = "polishwq"
S = [t[i:i + 4] for i in range(0, len(t), 4)]
# print(S)
v = ['a','e','i','o','u']
count = 0
for i in S[1 ]:
    for j in v:
        if j in i:
            print("word contains vowels")
#
# for i in range(len(S)):
#     for j in i:
#         print(j[i])
# if count > 0:
#     print("Yes")
