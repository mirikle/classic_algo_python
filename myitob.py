
def itob(itgr):
    rs = ''
    while itgr > 0:
        md = itgr % 2
        rs = str(md) + rs
        itgr = itgr / 2
    return rs

print(itob(128))