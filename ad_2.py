

with open("in.txt", "r") as f:
    x = f.read()
# print(x)
lines = x.split("\n")
# print(lines)

ls1 = []
ls2 = []
for line in lines:
    # print(line.split())
    try:
        l1 = line.split()[0]
        l2 = line.split()[1]
        ls1.append(int(l1))
        ls2.append(int(l2))
    except Exception as e:
        print(e)

print(ls1)
print(ls2)

# ss = 0
# for idx in range(len(ls1)):
#     m_ls1 = min(ls1)
#     ls1.remove(m_ls1)
#     m_ls2 = min(ls2)
#     ls2.remove(m_ls2)

#     mm = abs(int(m_ls1) - int(m_ls2))
#     ss += mm


ss = 0
for num in ls1:
    print(num)
    occr = ls2.count(num)
    ss+= (occr * num)


print(f"answer: {ss}")
