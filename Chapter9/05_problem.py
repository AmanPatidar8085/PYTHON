f=open("poem.txt")
content=f.read()
if("twinkle"in content):
    print("The word twinkle present in the content")
else:
    print("the word twinkle is not present in the content")
f.close()