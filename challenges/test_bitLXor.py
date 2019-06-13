import pytest
from bitLXor import bitLXor
#from sol_bitLXor import bitLXor
#from sol2_bitLXor import bitLXor


@pytest.mark.parametrize(("a", "b", "out"),[
    (5, 3, 3),
    (7, 1, 3),
    (-23, 7, -11),
    (2018, 255, 26),
    (1979, 2018, 89),
    (1, -1, -2),
    ])
def test_bitLXor(a, b, out):
    assert bitLXor(a, b) == out
