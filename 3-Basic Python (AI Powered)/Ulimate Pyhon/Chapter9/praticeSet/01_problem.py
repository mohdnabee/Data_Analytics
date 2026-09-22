f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word Twinkle is present in the Content")
else:    print("The word Twinkle is not present in the Content")

f.close()