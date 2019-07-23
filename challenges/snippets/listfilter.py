>>> L = ["", 1, 0, [5], [], None, (), (4, 2)]
>>> [x for x in L if x]
[1, [5], (4, 2)]
>>> filter(None,L)
