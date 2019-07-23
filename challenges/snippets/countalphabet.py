# Posted by: ArBo
# https://codegolf.stackexchange.com/questions/187207/alphabet-completion-rate

s="The quick brown fox jumps over the lazy dog"
#100%, 100, 1

# 46 bytes
f=lambda s:sum(map(str.isalpha,{*s.lower()}))/26
print(f(s))

# 42 bytes
f=lambda s:len({*s.upper()}-{*s.lower()})/26
print(f(s))


