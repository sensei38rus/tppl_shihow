def add(stack: list):
    b = stack.pop()
    a = stack.pop()
    stack.append(a + b)

def sub(stack: list):
    b = stack.pop()
    a = stack.pop()
    stack.append(a - b)

def mult(stack: list):
    b = stack.pop()
    a = stack.pop()
    stack.append(a * b)

def div(stack: list):
    b = stack.pop()
    a = stack.pop()
    if b == 0:
        raise ZeroDivisionError
    stack.append(a / b)

def special(stack: list):
    a = stack.pop()
    b = stack.pop()
    if a != 0 and b != 0:
        stack.append(abs(a - b))
    else:
        s = sum(stack) + a + b
        stack.append(s ** 2)


def posfix_calculation(expr: str):
    elements = expr.split()

    if not elements:
        raise ValueError("Empty expression")
    
    opers = {"+": add, "-": sub, "*": mult, "/": div, "~": special}
    stack = []
    count = 0
    for e in elements:
        if opers.get(e) is None:
            try:
                stack.append(float(e))
            except ValueError:
                raise ValueError("Invalid expression: not a number")
        else:
            if len(stack) < 2:
                raise ValueError("Not enough operands for operator")
            opers[e](stack)
        count += 1
        print(f"Stack state({count}): {stack}")

    return stack.pop()

if __name__ == "__main__":
    expression = input("Enter the expression: ")
    try:
        res = posfix_calculation(expression)
        print(f"({expression}) = {res}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: zero division")