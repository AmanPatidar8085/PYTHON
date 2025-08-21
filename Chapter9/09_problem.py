word =["Donkey","bad","good"]
with open("file1.txt","r") as f:
    content =f.read()
for word in word:
  content=content.replace(word,"#####")

with open("file1.txt","w") as f:
    f.write(content)