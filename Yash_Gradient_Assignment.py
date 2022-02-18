from sympy import *
def SolvePartialDifferention(X_point,Y_point):
    XY_value=list()
    x, y = symbols('x y', real=True)  
    equation = (x*y) - (sqrt(x)/2)
    Differentiate_equation=diff(equation,x)
    X_value=Differentiate_equation.subs([(x,X_point),(y,Y_point)])
    Differentiate_equation=diff(equation,y)
    Y_value=Differentiate_equation.subs([(x,X_point),(y,Y_point)])
    XY_value.append(X_value)
    XY_value.append(Y_value)
    return XY_value
X_point = input('Enter the value of X = ')
Y_point = input('Enter the value of Y = ')
if(X_point.isnumeric() and Y_point.isnumeric()):   
    Gradient=SolvePartialDifferention(X_point,Y_point)
    print(f"Gradient at X = {X_point} and Y = {Y_point} is = {str(Gradient):s}")
else:
    print('Enter Numeric values only')