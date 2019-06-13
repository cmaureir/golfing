# Submitted by paul_f10
def bitLXor(a, b):
    l = int.bit_length
    print(a,b)
    a,b = sorted([a,b],key=l)
    print(a,b)
    return a << l(b)-l(a) ^ b

print(bitLXor(5,3))
