import cmath
'''
   Bairstow's Method where:
      r = Initial guess
      s = Initial guess
     roots = Empty Array
   a = Coefficient's vector with increasing powers ot the unknown
   g = Polynomial's degree
'''
def bairstow(a,r,s,g,roots):
  if(g<1):
    return None
  if(g==1):
    roots.append(float(-a[0])/float(a[1]))
    return None
  if(g==2):
    D = (a[1]**2.0)-(4.0)*(a[2])*(a[0])
    X1 = (-a[1] - cmath.sqrt(D))/(2.0*a[2])
    X2 = (-a[1] + cmath.sqrt(D))/(2.0*a[2])
    roots.append(X1)
    roots.append(X2)
    return None
  n = len(a)
  b = [0]*len(a)
  c = [0]*len(a)
  b[n-1] = a[n-1]
  b[n-2] = a[n-2] + r*b[n-1]
  i = n - 3
  while(i>=0):
    b[i] = a[i] + r*b[i+1] + s*b[i+2]
    i = i - 1
  c[n-1] = b[n-1]
  c[n-2] = b[n-2] + r*c[n-1]
  i = n - 3
  while(i>=0):
    c[i] = b[i] + r*c[i+1] + s*c[i+2]
    i = i - 1
  Din = ((c[2]*c[2])-(c[3]*c[1]))**(-1.0)
  r = r + (Din)*((c[2])*(-b[1])+(-c[3])*(-b[0]))
  s = s + (Din)*((-c[1])*(-b[1])+(c[2])*(-b[0]))
  if(abs(b[0])>1E-8 or abs(b[1])>1E-8):
    return bairstow(a,r,s,g,roots)
  if (g>=3):
    Dis = ((-r)**(2.0))-((4.0)*(1.0)*(-s))
    X1 = (r - (cmath.sqrt(Dis)))/(2.0)
    X2 = (r + (cmath.sqrt(Dis)))/(2.0)
    roots.append(X1)
    roots.append(X2)
    return bairstow(b[2:],r,s,g-2,roots)
k = 0
roots = []
a = []
r = 100
s = -100
print("Degree?")
g = int(input(":"))
a.append(float(input("Constant: ")))
print("Input roots as a list,\nx^1 to x^n.")
for re in range(g) :
    a.append(float(input("x^" + str(re + 1) + ":")))
bairstow(a,r,s,g,roots)
print("\nFound Roots => \n")
for r in roots:
  print("R" + str(k) + " = " + str(r))
  k += 1
