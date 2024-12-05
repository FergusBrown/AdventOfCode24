def part1(a, b):
    sum = 0
    for i in range(len(a)):
        sum += abs(a[i] - b[i])

    print(sum)

def part2(a, b):
    freq = {}
    for n in b:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1

    sum = 0
    for n in a:
        if n in freq:
            sum += freq[n] * n

    print(sum)

if __name__ == "__main__":
    with open('i1') as f:
        lines = f.readlines()

    a = []
    b = []
    for l in lines:
        pair = l.split()
        a.append(int(pair[0]))
        b.append(int(pair[1]))

    a.sort()
    b.sort()
    part1(a, b)
    part2(a, b)
