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
    a = stack[len(stack)-1]
    b = stack[len(stack)-2]
    if a != 0 and b != 0:
        stack.pop()
        stack.pop()
        stack.append(abs(a - b))
    else:
        s = sum(stack)
        stack.append(s ** 2)

def validate_expression(elements: list, opers: dict) -> tuple[bool, str]:

    stack_size = 0
    for i, e in enumerate(elements, start=1):
        if e in opers:
            # Бинарные операторы требуют минимум 2 операнда на стеке
            if e == "~":
                if stack_size < 2:
                    return False, (f"Ошибка на позиции {i} ('{e}'): "
                                   f"для оператора '~' нужно минимум 2 операнда, "
                                   f"на стеке только {stack_size}")
            else:
                if stack_size < 2:
                    return False, (f"Ошибка на позиции {i} ('{e}'): "
                                   f"для оператора '{e}' нужно минимум 2 операнда, "
                                   f"на стеке только {stack_size}")
            stack_size -= 1  # два операнда -> один результат
        else:
            try:
                float(e)
                stack_size += 1
            except ValueError:
                return False, (f"Ошибка на позиции {i} ('{e}'): "
                               f"не является числом и не является оператором")
    if stack_size != 1:
        return False, (f"Некорректное выражение: в конце на стеке должно "
                       f"остаться 1 значение, а осталось {stack_size}")
    return True, ""

def posfix_calculation(inp: str):
    elements = inp.split()

    if not elements:
        raise ValueError("Пустое выражение")

    opers = {"+": add, "-": sub, "*": mult, "/": div, "~": special}

    # Проверка корректности ДО вычислений
    ok, err = validate_expression(elements, opers)
    if not ok:
        raise ValueError(err)

    stack = []
    count = 0
    for e in elements:
        if opers.get(e) is None:
            stack.append(float(e))
        else:
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
    except IndexError:
        print("Error: not enough operands")