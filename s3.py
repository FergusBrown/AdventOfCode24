import re

if __name__ == "__main__":
    with open('i3') as f:
        lines = f.readlines()

    p1 = 0
    p2 = 0
    enable = True
    for l in lines:
        p1_matches = re.findall("mul\((\d+),(\d+)\)", l)
        for m in p1_matches:
            p1 += int(m[0]) * int(m[1])

        p2_matches = re.findall("(don't\(\))|(do\(\))|mul\((\d+),(\d+)\)", l)
        for m in p2_matches:
            if m[1]:
                enable = True
            elif m[0]:
                enable = False
            elif enable:
                p2+= int(m[2]) * int(m[3])

    print(p1)
    print(p2)