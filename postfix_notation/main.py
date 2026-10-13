import sys

def add(a,b, stack: list):
    stack.append(a + b)

def sub(a,b,stack: list):
    stack.append(a - b)

def mult(a,b,stack: list):
    stack.append(a * b)

def div(a,b,stack: list):
    if b == 0:
        raise ZeroDivisionError
    stack.append(a / b)

def special(a,b,stack: list):
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
            b = stack.pop()
            a = stack.pop()
            opers[e](a,b,stack)
        count += 1
        print(f"Stack state({count}): {stack}")

    return stack.pop()

def main(): 
    if len(sys.argv) < 2:
        print("Usage: python3 main.py \"<expression>\"", file=sys.stderr)
        sys.exit(1)
    expression = sys.argv[1]
    try:
        res = posfix_calculation(expression)
        print(f"({expression}) = {res}")
    except ValueError as e:
        print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: zero division")

if __name__ == "__main__":
    main()