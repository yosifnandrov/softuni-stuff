import operator

def pars_expr(expr):
    n1, sign, n2 = expr.split()
    signs = {
        "/": operator.truediv,
        "*": operator.mul,
        "+": operator.add,
        "-": operator.sub,
        "^": operator.pow

    }
    sign = signs[sign]
    return sign, float(n1), int(n2)

def execute(operator, n1, n2):
    result = operator(n1,n2)
    return print(f"{result:.2f}")
