url = "https://google.com"

mystr = url.replace("https://", "")
mystr = mystr.replace(".com", "")

ni = mystr[:3] + str(len(mystr)) + str(mystr.count("e")) + "!"
print(ni)