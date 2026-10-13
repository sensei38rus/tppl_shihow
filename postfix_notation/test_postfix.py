import pytest
import main

def test_add():
    stack = [1,2,3]
    b = stack.pop()
    a = stack.pop()
    main.add(a,b,stack)
    assert([1,5] == stack)

def test_sub():
    stack = [1,2,3]
    b = stack.pop()
    a = stack.pop()
    main.sub(a,b,stack)
    assert([1,-1] == stack)

def test_mult():
    stack = [1,2,3]
    b = stack.pop()
    a = stack.pop()
    main.mult(a,b,stack)
    assert([1,6] == stack)

def test_div():
    stack = [1,6,2]
    b = stack.pop()
    a = stack.pop()
    main.div(a,b,stack)
    assert([1,3] == stack)

def test_special_zero():
    stack = [2,3,0]
    b = stack.pop()
    a = stack.pop()
    main.special(a,b,stack)
    assert([2,25] == stack)

def test_special_not_zero():
    stack = [1,2,3]
    b = stack.pop()
    a = stack.pop()
    main.special(a,b,stack)
    assert([1,1] == stack)

    stack2 = [1,3,2]
    b = stack2.pop()
    a = stack2.pop()
    main.special(a,b,stack2)
    assert([1,1] == stack2)

def test_simple_expression():
    exp1 = "3 4 +"
    assert(7 == main.posfix_calculation(exp1))

    exp2 = "5 4 -"
    assert(1 == main.posfix_calculation(exp2))

    exp3 = "2 3 *"
    assert(6 == main.posfix_calculation(exp3))

    exp4 = "6 2 /"
    assert(3 == main.posfix_calculation(exp4))

    exp5 = "3 5 ~"
    assert(2 == main.posfix_calculation(exp5))

def test_zero_div_expression():
    exp = "4 0 /"
    with pytest.raises(ZeroDivisionError):
        main.posfix_calculation(exp)

def test_invalid_expression():
    exp = "invalid expression / 2"
    with pytest.raises(ValueError):
        main.posfix_calculation(exp)

def test_empty_expression():
    exp =" "
    with pytest.raises(ValueError):
        main.posfix_calculation(exp)

def test_few_operands():
    exp = "2 * + -"
    with pytest.raises(ValueError):
        main.posfix_calculation(exp)


def test_complex_expression():
    exp1 = "3 4 + 2 * 7 /"
    assert(2 == main.posfix_calculation(exp1))

    exp2 = "1 2 + 3 4 + *"
    assert(21 == main.posfix_calculation(exp2))

    exp3 = "2 3 + 4 * 5 1 - -"
    assert(16 == main.posfix_calculation(exp3))

    exp4 = "100 2 3 + / 2 /"
    assert(10 == main.posfix_calculation(exp4))

    exp5 = "2 3 * 4 5 * +"
    assert(26 == main.posfix_calculation(exp5))

    exp6 = "2 3 4 * + 5 -"
    assert(9 == main.posfix_calculation(exp6))

    exp7 = "10 4 - 7 3 - * 2 /"
    assert(12 == main.posfix_calculation(exp7))

def test_special_expression():
    exp1 = "10 4 ~"
    assert(6 == main.posfix_calculation(exp1))

    exp2 = "4 10 ~"
    assert(6 == main.posfix_calculation(exp2))

    exp3 = "10 4 ~ 2 *"
    assert(12 == main.posfix_calculation(exp3))

    exp4 = "10 4 ~ 3 ~"
    assert(3 == main.posfix_calculation(exp4))

    exp5 = "10 4 ~ 10 4 ~ +"
    assert(12 == main.posfix_calculation(exp5))

    exp6 = "10 4 ~ 10 4 ~ *"
    assert(36 == main.posfix_calculation(exp6))

    exp7 = "1 2 ~ 3 4 ~ ~"
    assert(0 == main.posfix_calculation(exp7))

    exp8 = "100 30 ~ 20 5 ~ -"
    assert(55 == main.posfix_calculation(exp8))
