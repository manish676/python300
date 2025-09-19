# Compute gradients
import  sympy as sp

# Define A multivariable function

x, y = sp.symbols('x,y')
f = x**2 + 3*y**2 - 4*x*y

# compute partial derviatives
grade_x = sp.diff(f, x)
grade_y = sp.diff(f, y)
print("Gradients: ")
print("Grade X: ", grade_x)
print("Grade Y: ", grade_y)