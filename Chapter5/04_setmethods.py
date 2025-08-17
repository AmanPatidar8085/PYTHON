e=set()# dont use s={} as it will create a empty dictinary
s={1,6,4,7,44,4,4,44,4,4,"aman"}
print(s,type(s))
#                   add method
s.add("akshat")
print(s,type(s))

#              length method
b=len(s)
print(b)

#          remove method
s.remove(1)
print(s)

#       pop method
s.pop()
print(s)

#        clear method
s.clear()
print(s)

