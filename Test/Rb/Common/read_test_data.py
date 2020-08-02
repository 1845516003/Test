def read_txt(path):
    L = []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f:
            # 去除行中的换行符
            l1 = line.replace("\n", "")
            l2 = l1.split("|")
            L.append(l2)
    return L[1:]


def read_csv():
    pass