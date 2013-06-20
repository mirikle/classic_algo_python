def palindrome(seq):
    length = len(seq)
    for i in range(length / 2):
        if seq[i] != seq[length - i - 1]:
            return 0
    return 1

print palindrome('11211')