def is_safe(r):
    correct_dir = r[0] < r[1]
    safe = True
    fail_idx = 0
    for i in range(len(r) - 1):
        a = r[i]
        b = r[i+1]
        safe = safe and (a < b) == correct_dir
        diff = abs(a - b)
        safe = safe and (diff > 0 and diff < 4)
        if not safe:
            fail_idx = i
            break

    return (safe, fail_idx)

def part1(reports):
    count = 0
    for r in reports:
        if is_safe(r)[0]:
            count = count + 1
    
    return count

def part2(reports):
    count = 0
    for r in reports:
        result = is_safe(r)
        safe = result[0]
        fail_idx = result[1]
        if safe:
            count = count + 1
        else:
            try_i = [ fail_idx, fail_idx + 1]
            if fail_idx - 1 >= 0:
                try_i.append(fail_idx - 1)
            for i in try_i:
                retry = r.copy()
                retry.pop(i)
                if is_safe(retry)[0]:
                    count = count + 1
                    break

    return count

if __name__ == "__main__":
    with open('i2') as f:
        reports = [ [int(x) for x in l.split()] for l in f.readlines() ]

    print(part1(reports))
    print(part2(reports))
    
            
