import re

with open("in.txt", "r") as f:
    x = f.read()

# print(x)

dos = x.split("do()")
without_dont = ""

for item in dos:
    wdo = item.split("don't()")[0]
    without_dont += " " + wdo

matches = re.findall(r"mul\((\d{1,3},\d{1,3})\)", without_dont)
# print(matches)
for m in matches:
    print(m)
print(len(matches))
ss = 0
for ll in matches:
    # print(ll)
    ll:str
    nums = ll.split(",")
    # print(nums)
    l1 = int(nums[0])
    l2 = int(nums[1])
    ss += (l1 * l2)

print(ss)
