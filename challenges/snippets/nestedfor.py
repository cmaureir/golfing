for i in range(m):
    for j in range(n):
        do_stuff(i,j)


for k in range(m*n):
  do_stuff(k//n,k%n)
