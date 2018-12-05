from math import *
while True :
  print("============")
  print("1. Interest")
  print("2. GeoSum")
  print("3. Annuity")
  print("4. Schedule")
  print("9. Exit")
  choice = int(input(":"))
  if choice == 1 :
    print("A*(1+b/c)^x*c")
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    x = float(input("X: "))
    y = float((a * ((1+(b/c))**(x*c))))
    print("You will have",y)
    print("after",x,"years.")
  if choice == 2 :
    al = float(input("PV: "))
    an = float(input("FV: "))
    c = float(input("Compounded: "))
    step = float(input("Dec. %: "))
    an = (log((an/al),(1+(step/c))))/c
    print("Iterations: " + str(an))
    sn = ((al*(1-step**an)))/(1-step)
    print("Sum: " + str(sn))
  if choice == 3 :
    print("FV=(PMT/i)[(1+i)^n -1](1+iT)")
    print("r = R/100, n = mt, i = r/m")
    qs = ["Future V?","Payment?","Percentage?","Type? 0 = Ord.","# of Periods?","Compounded?"]
    inputs = []
    for u in range(6) :
      print(qs[u])
      inputs.append(float(input(":")))
    r = float(inputs[2]/100)
    n = float(inputs[4]*inputs[5])
    i = float(r/inputs[5])
    if inputs[0] == 0 :
      ans = float((inputs[1]/i)*(((1+i)**n)-1)*(1+(i*inputs[3])))
    if inputs[1] == 0 :
      ans = float((inputs[0]/((((1+i)**n)-1)*(1+(i*inputs[3]))))*i)
    print(ans)
  if choice == 4 :
    print("Loan?")
    p = float(input(":"))
    print("Rate? 4 = 4%")
    i = float(input(":"))
    print("Time?")
    n = float(input(":"))
    print("Compounded?")
    c = float(input(":"))
    print("Extra?")
    e = float(input(":"))
    output=[]
    annuity = (((i/100)/c)*p)/(1-((1+((i/100)/c))**(-(n*c))))
    print(annuity)
    nc = int(n*c)
    i = (i/100)/c
    def sh(listNum,c,low,high):
      k = p
      global i
      global e
      global totalI
      totalI = 0
      r = 0
      while k > 0 :
        interest = k*i
        principal = annuity - interest
        k = (k-principal)-e
        if c == 5 :
            totalI = totalI+interest
        elif (r >= low) and (r <= high) :
          if c == 1 :
            listNum.append(round(k,3))
          if c == 2 :
            listNum.append(round(principal,3))
          if c == 3 :
            listNum.append(round(interest,3))
        r = r+1
    stop = 0
    while stop == 0 :
      sh(output,5,0,0)
      print(totalI)
      print("Print K, P, I, or Exit?")
      choice = int(input("1,2,3,4:"))
      if choice == 4 :
          stop = 1
      else :
          print("Range?(m#,m#):")
          rangeA = []
          rangeA.append(int(input("Low:")))
          rangeA.append(int(input("High:")))
          sh(output,choice,rangeA[0],rangeA[1])
          print(output)
  if choice == 9 :
    break
