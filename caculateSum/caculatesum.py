import numpy as np

c,h = 50,30

values = []
items = [x for x in input("Enter numbers: ").split(",")]

for d in items:
    values.append(str(int(round(np.sqrt(2*c*float(d)/h)))))

print(",".join(values))
