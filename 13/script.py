import sys
sys.path.append('../utils')
from utils import *
from pyomo.environ import *
import logging
logging.getLogger('pyomo.core').setLevel(logging.ERROR)

lines = read_data()
res = 0
newModel = True
for line in lines:
    if line == '':
        continue
    else:
        if line.startswith('Button A'):
            newModel = False
            model = ConcreteModel()
            model.a = Var(domain=PositiveIntegers)
            model.b = Var(domain=PositiveIntegers)
            _, d = line.split(':')
            a, b = line.split(',')
            _, xnumA = a.split('+')
            _, ynumA = b.split('+')
            xnumA, ynumA = int(xnumA), int(ynumA)
        elif line.startswith('Button B'):
            _, d = line.split(':')
            a, b = line.split(',')
            _, xnumB = a.split('+')
            _, ynumB = b.split('+')
            xnumB, ynumB = int(xnumB), int(ynumB)
        else:
            _, d = line.split(':')
            a, b = line.split(',')
            _, x = a.split('=')
            _, y = b.split('=')
            x, y = int(x), int(y)
            model.cost = Objective(expr = 3 * model.a + model.b, sense=minimize)
            model.constrx = Constraint(expr = xnumA * model.a + xnumB * model.b == x)
            model.constry = Constraint(expr = ynumA * model.a + ynumB * model.b == y)
            opt = SolverFactory('glpk')
            opt.solve(model)
            if model.a() != None:
                res += int(model.cost())
print(res)
copy_result(res)
