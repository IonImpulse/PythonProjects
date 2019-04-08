def stampToSeconds() :
    stamp = str(input(":"))
    format = int(stamp.count(":"))
    print(format)
    if format == 0 :
        return(str(int(format) * 1000))
    elif format == 1 :
        pos = [pos for pos, char in enumerate(stamp) if char == ":"]
        tempSec = int(stamp[:pos[0]]) * 60000
        tempSec += int(stamp[pos[0]+1:]) * 1000
        return(str(tempSec))
    elif format == 2 :
        pos = [pos for pos, char in enumerate(stamp) if char == ":"]
        tempSec = int(stamp[:pos[0]]) * 3600000
        tempSec += int(stamp[pos[0]+1:pos[1]]) * 60000
        tempSec += int(stamp[pos[1]+1:]) * 1000
        return(str(tempSec))

text_file = open("metadata.txt", "w")
text_file.write(";FFMETADATA\n")
print("Rolling timestamps? Y/n")
choice = str(input(":"))
print("Title?")
title = input(":")
writeString = "title=" + str(title)
text_file.write(writeString)
print("How many chapters?")
chapterCount = int(input(":"))
for i in range(chapterCount) :
    print("Chapter " + str(i+1) + " Name?")
    title = str(input(":"))
    print("Start?")
    writeString = stampToSeconds()
    if (choice == "Y" or choice == "y") and i != 0 :
        text_file.write("\nEND=")
        text_file.write(str(int(writeString)-1))
    text_file.write("\n\n")
    text_file.write("[CHAPTER]\n")
    text_file.write("TIMEBASE=1/1000\n")
    text_file.write("START=")
    text_file.write(writeString)
    if choice != "Y" and choice != "y" and i != 0 :
        print("End?")
        text_file.write("\nEND=")
        writeString = str(int(stampToSeconds())-1)
        text_file.write(writeString)
    text_file.write("\ntitle=")
    text_file.write(title)
text_file.close()
