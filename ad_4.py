import re


with open("in.txt", "r") as f:
    x = f.read()
# print(x)
lines = x.split("\n")
# print(lines)


ss = 0
l = len(lines[0])
print(l)

fwd = ""
for line in lines:
    fwd+=line + " "
# print(fwd)

print(len(fwd))
ss+= len(re.findall("XMAS", fwd))
ss+= len(re.findall("SAMX", fwd))


vert = ""
for num in range(l):
    for line in lines:
        for idx, ch in enumerate(line):
            if idx%l == num:
                vert+=ch
    vert+= " "
print(len(vert))
ss+= len(re.findall("XMAS", vert))
ss+= len(re.findall("SAMX", vert))


def find_diag(index: int, rest_lines: list):
    diag = ""
    for line in rest_lines:
        if line != "":
            index+=1
            if index < len(line):
                diag+=line[index]
    return diag

diag = ""
# for 1st line
for l_n, line in enumerate(lines):
    for ind, ch in enumerate(line):
        if l_n > 0 and ind > 0:
            continue
        diag+=ch
        diag+=find_diag(ind, lines[l_n+1:])
        diag+=" "
print(len(diag))


ss+= len(re.findall("XMAS", diag))
ss+= len(re.findall("SAMX", diag))


lines.reverse()


diag3 = ""
# for 1st line
for l_n, line in enumerate(lines):
    for ind, ch in enumerate(line):
        if l_n > 0 and ind > 0:
            continue
        diag3+=ch
        diag3+=find_diag(ind, lines[l_n+1:])
        diag3+=" "
print(len(diag3))

ss+= len(re.findall("XMAS", diag3))
ss+= len(re.findall("SAMX", diag3))




# print(diag)
# print(diag3)


print(ss)




# ii=0

# not_x=0
# not_y=0
# not_xmas=0

# def is_mas(x, y, lines):
#     global not_x, not_y, not_xmas
#     if x-1 < 0 or x+1>=len(lines[0]):
#         # print(f"xx {x}, {y}")
#         not_x+=1
#         return False
#     if y-1 < 0 or y+1>=len(lines):
#         # print(f"yy {x}, {y}")
#         not_y+=1
#         return False

#     x1 = lines[y-1][x-1] + lines[y][x] + lines[y+1][x+1]
#     x2 = lines[y-1][x+1] + lines[y][x] + lines[y+1][x-1]
#     # if x == 1 and y == 8:
#     #     breakpoint()

#     if x1 in ["MAS", "SAM"] and x2 in ["MAS", "SAM"]:
#         print(f"{x1}..{x2}")
#         return True
#     else:
#         not_xmas+=1
#         pass
#         print(f"{x} {y}  {x1}.--.{x2}")
#     return False


# for y, line in enumerate(lines):
#     for x, ch in enumerate(line):
#         if is_mas(x,y, lines):
#             ii+=1


# print(f"ii:  {ii}")

# print(f"not_x.{not_x}")
# print(f"not_y.{not_y}")
# print(f"not_xmas.{not_xmas}")
