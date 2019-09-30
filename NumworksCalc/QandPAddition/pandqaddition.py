import math

cubicFunction = []
linFunction = []

print("======P + Q Solver======")
print("Step 1: Cubic Function")
print("x^3 + ax + b")
print("a?")
cubicFunction.append(float(input(":")))
print("b?")
cubicFunction.append(float(input(":")))

print("Step 2: Linear")
print("Xp?")
linFunction.append(float(input(":")))
print("Yp?")
linFunction.append(float(input(":")))
print("Xq?")
linFunction.append(float(input(":")))
print("Yq?")
linFunction.append(float(input(":")))

linSlope = (linFunction[0]-linFunction[2])/(linFunction[1]-linFunction[3])
linIntercept = linFunction[1] - (linSlope * linFunction[0])

#Xr here
linFunction.append(linSlope - linFunction[0] - linFunction[2])

#Xy here
linFunction.append((linSlope * linFunction[4]) + linIntercept)

print("\nP + Q:")
print("X = " + str(linFunction[4]) + "\nY = " + str(-1 * linFunction[5]))
