while True :
    text = input("Text? ")
    
    output = ""

    for i in text :
        if i == " " :
            output += "  "
        else :
            output += f":regional_indicator_{i}: "
    
    print(output)