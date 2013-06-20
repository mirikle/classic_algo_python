def reduce_rpn(seq):
    prev = 2 ** 31
    cur = len(seq)
    while prev > cur:
        seq = seq.replace('xx*', 'x')
        prev = cur
        cur = len(seq)
    return seq

tests = ['x', 'xx*', 'xxx**', '*xx', 'xx*xx**', 'x**x*', 'xx*x*']
for test in tests:
    seq = reduce_rpn(test)
    print seq
    print len(seq) - 1
