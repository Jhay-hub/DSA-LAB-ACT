"""ITECC04 Laboratory 4, Parts B and C: the converter and the evaluator.

Part B turns infix into postfix using the Shunting Yard algorithm.
Part C evaluates a postfix expression.

Both use your own stack. Import it, do not use a bare Python list. If your
ArrayStack is not finished, these functions cannot work, so finish Part A
first.

TOKENS ARE SEPARATED BY SPACES. "3 + 4" is valid input, "3+4" is not. This
is deliberate: writing a real tokeniser is a different exercise, and mixing
it in here hides the algorithm you are meant to be learning.
"""

from stack_array import ArrayStack

# Written for you. Higher number binds tighter.
PRECEDENCE = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

# Written for you. 2 ^ 3 ^ 2 means 2 ^ (3 ^ 2), not (2 ^ 3) ^ 2.
RIGHT_ASSOCIATIVE = {"^"}


def tokenize(expression):
    """Written for you. Splits on whitespace."""
    return expression.split()


def infix_to_postfix(expression):
    """Step 1. Convert infix to postfix. Return a space-separated string."""
    output = []
    operators = ArrayStack()

    for token in tokenize(expression):
        if token == "(":
            operators.push(token)

        elif token == ")":
            while True:
                if operators.is_empty():
                    raise ValueError("unbalanced parentheses: no matching '('")
                top = operators.pop()
                if top == "(":
                    break
                output.append(top)

        elif token in PRECEDENCE:
            while (not operators.is_empty()
                   and operators.peek() != "("
                   and _outranks(operators.peek(), token)):
                output.append(operators.pop())
            operators.push(token)

        else:
            output.append(token)

    while not operators.is_empty():
        top = operators.pop()
        if top == "(":
            raise ValueError("unbalanced parentheses: no matching ')'")
        output.append(top)

    return " ".join(output)


def _outranks(stacked, incoming):
    """True when the stacked operator must come off before `incoming` goes on.

    Strictly higher precedence always comes off. Equal precedence also comes
    off, unless the incoming operator is right associative -- that is what
    makes 2 ^ 3 ^ 2 group to the right.
    """
    if PRECEDENCE[stacked] > PRECEDENCE[incoming]:
        return True
    return (PRECEDENCE[stacked] == PRECEDENCE[incoming]
            and incoming not in RIGHT_ASSOCIATIVE)


def evaluate_postfix(expression):
    """Step 2. Evaluate a postfix expression. Return a float."""
    values = ArrayStack()

    for token in tokenize(expression):
        if token in PRECEDENCE:
            if values.size() < 2:
                raise ValueError(
                    "not enough operands for operator '%s'" % token)
            right = values.pop()
            left = values.pop()
            values.push(apply_operator(token, left, right))
        else:
            values.push(float(token))

    if values.is_empty():
        raise ValueError("empty expression")
    result = values.pop()
    if not values.is_empty():
        raise ValueError("too many operands: leftover values on the stack")
    return result


def apply_operator(operator, left, right):
    """Step 3. Return the result of `left operator right`."""
    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            raise ZeroDivisionError("division by zero")
        return left / right
    if operator == "%":
        if right == 0:
            raise ZeroDivisionError("modulo by zero")
        return left % right
    if operator == "^":
        return left ** right
    raise ValueError("unknown operator '%s'" % operator)


def convert_and_evaluate(expression):
    """Written for you. Used by the test file and by the classwork demo."""
    postfix = infix_to_postfix(expression)
    return postfix, evaluate_postfix(postfix)


if __name__ == "__main__":
    try:
        postfix, value = convert_and_evaluate("3 + 4 * 2")
        print("infix   : 3 + 4 * 2")
        print("postfix :", postfix)
        print("value   :", value)
    except NotImplementedError as unfinished:
        print("Not written yet ->", unfinished)