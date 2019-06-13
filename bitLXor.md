(Source CodeSignal)
All of you may know that when doing bit XOR we are doing it from the right side. Here is the example:

```
     101 (decimal 5)
XOR   11 (decimal 3)
  =  110 (decimal 6)
```

But in this challenge bitLXor, you will need to do it from the left. Left take the above example:

```
     101 (decimal 5)
LXOR 11  (decimal 3)
   = 011 (decimal 3)
```

Provided 2 numbers a and b, return value of the LXOR operation.

Example
For a = 5 and b = 3, the output should be
bitLXor(a, b) = 3.

Input/Ouput

```
    [execution time limit] 4 seconds (py3)

    [input] integer a

    Guaranteed constraints:
    -231 < a < 231.

    [input] integer b

    Guaranteed constraints:
    -231 < b < 231.

    [output] integer
```

