import sys
import itertools
from z3 import *

s = Solver()

x = Int("x")
y = Int("y")
z = Int("z")

s.add(x > 0)
s.add(y > 0)
s.add(z > 0)
s.add(Distinct([x, y, z]))
#s.add(Distinct(y))
s.add(x + y <= z + x)

if s.check() == sat:
    m = s.model()
    print m
