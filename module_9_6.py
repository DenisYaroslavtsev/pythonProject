def all_variants(text):
    n = len(text)
    for i in range(n):
        for j in range(n - i):
            yield text[j:j + i + 1]

a = all_variants("abc")
for i in a:
    print(i)