def count_xmas(line):
    count = line.count("XMAS")
    count += line.count("SAMX")
    return count

def get_diag(point, dir, lines):
    max = (len(lines[0]), len(lines))
    result = ""
    next = point
    while next[0] < max[0] and next[1] < max[1] and next[0] >= 0 and next[1] >= 0:
        result += lines[next[1]][next[0]]
        next = (next[0]+dir[0], next[1]+dir[1])
    return result

def part1(lines):
    count = 0
    # horizontal
    for l in lines:
        count += count_xmas(l)

    # vertical
    for i in range(len(lines)):
        vert = ''.join([l[i] for l in lines])
        count += count_xmas(vert)

    # diag
    for i in range(len(lines)):
        # skip first index for these to avoid a duplicate evaluation
        if i > 0:
            # from top
            diag = get_diag((i,0), (1,1), lines)
            count += count_xmas(diag)

            # from bottom
            diag = get_diag((i,len(lines)-1), (1,-1), lines)
            count += count_xmas(diag)

        # from top reverse
        diag = get_diag((i,0), (-1,1), lines)
        count += count_xmas(diag)
        
        # from bottom reverse
        diag = get_diag((i,len(lines)-1), (-1,-1), lines)
        count += count_xmas(diag)


    print(count)

def get_mas_locs(line: str):
    mas_locs = []
    idx = 0
    while True:
        try:
            idx = line.index("MAS", idx)
            mas_locs.append(idx+1)
            idx+=3
        except:
            break

    idx = 0
    while True:
        try:
            idx = line.index("SAM", idx)
            mas_locs.append(idx+1)
            idx+=3
        except:
            break

    return mas_locs

def part2(lines):
    count = 0
    left = []
    right = []
    for i in range(len(lines)):
        # skip first index for these to avoid a duplicate evaluation
        start_top = (i,0)
        start_bot = (i,len(lines)-1)
        if i > 0:
            # from top
            dir = (1,1)
            diag = get_diag(start_top, dir, lines)
            right.extend([((start_top[0]+dir[0]*loc, start_top[1]+dir[1]*loc)) for loc in get_mas_locs(diag)])

            # from bottom
            dir = (1,-1)
            diag = get_diag(start_bot, dir, lines)
            left.extend([((start_bot[0]+dir[0]*loc, start_bot[1]+dir[1]*loc)) for loc in get_mas_locs(diag)])


        # from top reverse
        dir = (-1,1)
        diag = get_diag(start_top, dir, lines)
        left.extend([((start_top[0]+dir[0]*loc, start_top[1]+dir[1]*loc)) for loc in get_mas_locs(diag)])

        # from bottom reverse
        dir = (-1,-1)
        diag = get_diag(start_bot, dir, lines)
        right.extend([((start_bot[0]+dir[0]*loc, start_bot[1]+dir[1]*loc)) for loc in get_mas_locs(diag)])

    count = len(set(left) & set(right))
    
    print(count)

if __name__ == "__main__":
    with open('i4') as f:
        lines = [l.strip() for l in f.readlines()]

    part1(lines)
    part2(lines)
