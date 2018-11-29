unleet = "null"
leet = "null"

while unleet != "Exit" or "exit":
  unleet = input("What should I make l33t?")
  print(unleet)
  leet = unleet
  for x in len(leet):
      if leet[x] == "e":
          leet[x] = "3"
      if leet[x] == "t":
          leet[x] = "8"
          
