import time

def gen_pwd(x):

    def toHex(dec):
        x = (dec % 16)
        digits = "0123456789ABCDEF"
        rest = dec / 16
        if (rest == 0):
            return digits[x]
        return toHex(rest) + digits[x]

    for x in range(x):
        print toHex(x) 
    f = open("test.txt")
    print f
    value = x
    string = str(value)
    f.write(string) 

start= time.time()
#gen_pwd()
last=time.time()-start
print last
