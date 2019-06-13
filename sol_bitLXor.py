def bitLXor(a, b):
    l = len(bin(a))-len(bin(b))
    l = (l,l-1)[a<0]
    b = b<<l if l>0 else b
    a = a<<l*-1 if l<-1 else a
    return a^b
