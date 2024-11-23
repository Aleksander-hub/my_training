

def all_variants(text):
    txt = len(text)

    for i in range(1, txt + 1):
        for j in range(txt - i + 1):
            end = j + i
            res = text[j:end]
            yield res


a = all_variants("abc")
for i in a:
    print(i)

# шарик ты балбес!




