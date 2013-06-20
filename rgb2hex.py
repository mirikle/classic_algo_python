rgb = (128, 255, 255)

#for i in range(0, 128):
#    print chr(i), 
    

def tohex(i):
    if i == 0: return '0'
    ret = "";
    while(i != 0):
        tmp = i % 16
        ch = '0'
        if(tmp > 10):
            tmp -= 10
            ch = 'A'
        ret = chr(tmp + ord(ch)) + ret
        i /= 16
    return ret
    
ret = "0x"
for i in rgb:
    ret += tohex(i)
print ret
