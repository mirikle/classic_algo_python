mapping = ["", "ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VW", "XY", "Z*#"]

def combinations(res, digits, idx, results):
    if idx == len(digits): 
        results.append(''.join(res))
        return
    digit = digits[idx]
    letters = mapping[digit]
    for i in range(len(letters)):
        res[idx] = letters[i]
        combinations(res, digits, idx + 1, results)

digits = [1, 2, 3, 4]
results = []
combinations(['' for i in range(len(digits))], digits, 0, results)
print results
print len(results)
    

