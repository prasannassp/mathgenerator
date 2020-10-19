from .__init__ import *


def volumeCylinder(maxRadius=20, maxHeight=50, unit='m'):
    a = random.randint(1, maxHeight)
    b = random.randint(1, maxRadius)
    
    problem = f"Volume of cylinder with height = {a}{unit} and radius = {b}{unit} is"
    ans = int(math.pi * b * b * a)
    solution = f"{ans} {unit}^3"
    return problem, solution
