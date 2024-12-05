

with open("in.txt", "r") as f:
    x = f.read()
# print(x)
lines = x.split("\n")
# print(lines)

lists = []
for line in lines:
    l = [int(x )for x in line.split()]
    if len(l) != 0:
        lists.append(l)

# print(lists)

def is_safe(l):
    safe = True
    sig = 1 if (l[1] - l[0]) > 0 else -1
    for idx in range(len(l)-1):
        diff = l[idx + 1] - l[idx]
        # print(diff)
        if diff*sig > 0:
            pass # same sign
        else:
            print(f"diff{diff}, sign{sig}")
            safe = False
            return False
        if abs(diff) >= 1 and abs(diff)<=3:
            pass
        else:
            print(f"diff{diff}")
            safe = False
            return False
    return True

safes = 0
for l in lists:
    if is_safe(l):
        safes+=1
    else:
        for id in range(len(l)):
            l:list
            l_new = l.copy()
            l_new.pop(id)
            if is_safe(l_new):
                safes+=1
                break

print(safes)
