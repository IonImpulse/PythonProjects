unleet = "null"
leet = "null"

while unleet != "Exit" or "exit":
  print("What should I make l33t?")
  unleet = input(":")
  leet = ""
  for x in unleet:
      if x == "e":
          leet = leet + "3"
      if x == "t":
          leet = leet + "8"
      else :
          leet = leet + x
  print(leet)
