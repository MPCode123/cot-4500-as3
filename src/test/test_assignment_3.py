import sys
import os

# For using functions from assignment_1 to test in test_assignment_1
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.main.assignment_3 import *

# Function
def f(t,y):
    return t - y**2

# Euler Method
# Range: 0 < t < 2
# Iterations: 10
# Initial Point: f(0) = 1
# h = (2 - 0) / 10 = 0.2

Euler(0,1,f,0.2,10) # 1.2446380979332121


print("\n")


# Runge-Kutta
# Range: 0 < t < 2
# Iterations: 10
# Initial Point: f(0) = 1
# h = (2 - 0) / 10 = 0.2

RK(0,1,f,0.2,10) # 1.251316587879806

