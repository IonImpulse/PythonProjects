print("Welcome to PQDSCR!")
print("==================")
print("q = a * p + b")
qa = float(input("a: "))
qb = float(input("b: "))
print("p = a * q + b")
pa = float(input("a: "))
pb = float(input("b: "))
b = (qb-(pa*qa))
c = 0-((pa*qb) + pb)
print("Profit =",qa,"p^2 +",b,"+",c)
ans1 = (-b + ((b**2) - 4*qa*c)**(1/2.0))/(2*qa)
ans2 = (-b - ((b**2) - 4*qa*c)**(1/2.0))/(2*qa)
print("Zero #1: ",ans1)
print("Zero #2: ",ans2)
vx = (ans1 + ans2)/2
vy = (qa*(vx**2)) + (b*vx) + c
print("Vertex: ",vx,vy)
