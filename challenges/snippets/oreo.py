# Submitted by: Riker
# https://codegolf.stackexchange.com/questions/178344/oreoorererereoo
# Modified
l=len
n="\n"
f=lambda x:x.replace("o","░"*l(x)+n).replace("re"," "+'█'*(l(x)-2)+n)
i = input()
print(f(i))
