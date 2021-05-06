import mathops

expr = input()

operator, n1,n2 = mathops.pars_expr(expr)
mathops.execute(operator,n1,n2)