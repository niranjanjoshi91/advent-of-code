import re

with open("in.txt", "r") as f:
    x = f.read()
# print(x)
# lines = x.split("\n")
# print(lines)


ans = 0

rules = re.findall(r"(\d+\|\d+)", x)
# print(rules)
r = [(r.split("|")[0], r.split("|")[1]) for r in rules]
# print(fst)
# print(r)
d = dict()

for a,b in r:
    if a in d.keys():
        d[a].append(b)
    else:
        d[a] = [b]

# print(d)


upd = re.findall(r"((?:\d+,)+\d+)\n", x)
# print(upd)


def reorder(pages):
    new = []
    # print(pages)
    for page in pages:
        id = 10000000
        if page in d.keys():
            snd = d[page]
            for s in snd:
                try:
                    id = min(new.index(s), id)
                except ValueError:
                    pass
                    # print(f"e:{s}")
        print(id)
        new = new[:id] + [page] + new[id:]
    print(new)
    return new



l = []
md = []
for pp in upd:
    pages = pp.split(",")
    good = True
    for idx, page in enumerate(pages):
        # print(page)
        if page in d.keys():
            snd = d[page]
            for s in snd:
                if s in pages[:idx]:
                    good = False
    if good != True:
        pass
        # pr = pages
        pr = reorder(pages)
        l.append(pr)
        ln = len(pr)
        m = int(ln/2)
        md.append(int(pr[m]))
    else:
        pass
        # pr = pages
        # l.append(pr)
        # ln = len(pr)
        # m = int(ln/2)
        # md.append(int(pr[m]))

# print(l)
# print(md)
ans = sum(md)







print(f"answer: {ans}")