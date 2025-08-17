marks = {
    "Aman":85,
    "Akashat":67,
    "Hariom":74,
    "Ajay":74
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aman":95})
print(marks)
print(marks.get("Aman1"))# print none
#print(marks["Aman1"])# error
print(marks.popitem())
print(marks)
print(marks.popitem())
print(marks)