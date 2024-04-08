import math

def figure_area(args):
    figure_type = args[0]
    if figure_type == 'circle':
        if len(args) != 2:
            print("The number of arguments for calculating the area of a circle is incorrect.")
            res = 0
        else:
            rad = float(args[1])
            if rad <= 0:
                print("The radius must be a positive number.")
                res = 0
            else:
                res = math.pi * rad**2
    
    elif figure_type == 'triangle':
        if len(args) != 4:
            print("The number of arguments for calculating the area of a triangle is incorrect.")
            res = 0
        else:
            side1 = float(args[1])
            side2 = float(args[2])
            side3 = float(args[3])
            if side1 <= 0 or side2 <= 0 or side3 <= 0 :
                print("The lengths of the sides of the triangle must be positive numbers.")
                res = 0
            else:
                p = (side1 + side2 + side3) / 2
                res = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    else:
        print("Figure type entered incorrectly")
        res = 0
    return res

print("""Enter the name of the figure and the necessary data for the calculation.
Now a circle and a triangle are available.
For a circle, enter 1 parameter - radius.
For a triangle, enter 3 parameters - the lengths of 3 sides.""")
area = figure_area(input().split())
if area > 0:
    print(f"The area of your figure is {area: .2f}")