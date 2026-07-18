from src.mathoperators import  add,sub
def test_add():
    assert add(2,3) == 5
    assert add(5,6) == 11
    assert add(3,3) == 6

def test_sub():
    assert sub(2,3) == -1
    assert sub(5,6) == 1
    assert sub(3,3) == 0