def high(bp):
    return max(bp) , min(bp)

def avg(bp):
    avg = sum(bp) / len(bp)
    return avg

def count_high(bp):
    count = 0
    for i in bp:
        if i > 140:
            count += 1
    return count