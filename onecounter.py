
def countone(val):
    counter = 0
    while val != 0:
        val = val & (val - 1)
        counter += 1
    return counter



for i in range(10):
    print countone(i)