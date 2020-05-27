h = list(map(int, input().split()))
dict = {}
j = 0
for i in range(97,123):
    dict[chr(i)] = h[j]
    j += 1
word = input()
word = list(word)
wordvalues = []
for i in dict.keys():
    if i in word :
        wordvalues.append(dict[i])
print(len(word) * max(wordvalues))
