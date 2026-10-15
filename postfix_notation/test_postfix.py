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
    assert [1,-1] == stack 

def test_mult():
    stack = [1,2,3]
    b = stack.pop()
    a = stack.pop()
    main.mult(a,b,stack)
    assert [1,6] == stack 

def test_div():
    stack = [1,6,2]
    b = stack.pop()
    a = stack.pop()
    main.div(a,b,stack)
    assert [1,3] == stack 

def test_special_zero():
    stack = [2,3,0]
    b = stack.pop()
    a = stack.pop()
    main.special(a,b,stack)
    assert [25] == stack 
def test_special_not_zero():
    stack = [2,3]
    b = stack.pop()
    a = stack.pop()
    main.special(a,b,stack)
   
    stack2 = [3,2]
    b = stack2.pop()
    a = stack2.pop()
    main.special(a,b,stack2)
    
    assert stack == stack2 == [1]


def test_add_expression():
    exp1 = "2 5 +"
    assert 7 == main.posfix_calculation(exp1)

    exp2 = "1 2 3 + +"
    assert 6 == main.posfix_calculation(exp2)

    exp3 = "1 2 + 5 +"
    assert 8 == main.posfix_calculation(exp3)

def test_sub_expression():
    exp1 = "5 2 -"
    assert 3 == main.posfix_calculation(exp1)

    exp2 = "2 5 -"
    assert -3 == main.posfix_calculation(exp2)

    exp3 = "5 2 3 - -"
    assert 6 == main.posfix_calculation(exp3)

def test_mult_expression():
    exp1 = "2 5 *"
    assert 10 == main.posfix_calculation(exp1)

    exp2 = "2 5 3 * *"
    assert 30 == main.posfix_calculation(exp2)

    exp3 = "2 3 * -4 *"
    assert -24 == main.posfix_calculation(exp3)

def test_div_expression():
    exp1 = "10 2 /"
    assert 5 == main.posfix_calculation(exp1)

    exp2 = "2 10 /"
    assert 0.2 == main.posfix_calculation(exp2)

    exp3 = "10 20 2 / /"
    assert 1 == main.posfix_calculation(exp3)

def test_special_not_zero_expression():
    exp1 = "1 4 ~"
    assert 3 == main.posfix_calculation(exp1)

    exp2 = "4 1 ~"
    assert 3 == main.posfix_calculation(exp2)

    exp3 = "10 4 ~ 3 ~"
    assert 3 == main.posfix_calculation(exp3) 
 
def test_special_zero_expression():
    exp1 = "3 0 4 ~ 2 ~"
    assert 47 == main.posfix_calculation(exp1)

    exp2 = "5 0 ~"
    assert 25 == main.posfix_calculation(exp2)

    exp3 = "2 3 0 ~ 5 ~"
    assert 20 == main.posfix_calculation(exp3)

def test_complex_expression():
    exp1 = "3 4 + 2 * 7 /"
    assert 2 == main.posfix_calculation(exp1) 

    exp2 = "2 2 + 4 - 4 ~ 2 3 * +"
    assert 22 == main.posfix_calculation(exp2)

    exp3 = "2 3 + 4 * 5 - 6 / 0 ~"
    assert 6.25 == main.posfix_calculation(exp3)

    exp4 = "3 0 4 ~ 2 ~ 5 + 6 * 7 - 8 /"
    assert 38.125 == main.posfix_calculation(exp4)

 

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
    exp1 = "2 * + -"
    with pytest.raises(ValueError):
        main.posfix_calculation(exp1)

    exp2 = "4 2 / 3 0 ~ 5 - * 6 +"
    with pytest.raises(ValueError):
            main.posfix_calculation(exp2)

    exp3 = "5 5 * 2 / 3 0 ~ 4 - +"
    with pytest.raises(ValueError):
            main.posfix_calculation(exp3)



