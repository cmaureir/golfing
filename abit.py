def alienBit(abit):
    s = ""
    for i in range(2, len(abit), 3):
        s += chr(int(abit[i:i+3]))
    return s

abit = "0.116101115116035049"
assert alienBit(abit) == "test#1"

abit = "0.073110099111109105110103032084114097110115109105115105111110"
assert alienBit(abit) == "Incoming Transmision"

abit = "0.116101115116105110103046046046032049050051052053054055056057049048"
assert alienBit(abit) == "testing... 12345678910"

