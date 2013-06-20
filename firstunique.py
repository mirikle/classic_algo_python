def funi(seq):
    cnt = [0 for i in range(26)]
    for ch in seq:
        cnt[ord(ch) - ord('a')] += 1
    for ch in seq:
        if cnt[ord(ch) - ord('a')] == 1:
            print ch
            break
funi('aabacacd')