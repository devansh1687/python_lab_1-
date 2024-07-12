maths = int(input("Enter maths marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))
history = int(input("Enter history marks: "))
geography = int(input("Enter geography marks: "))

total = maths + science + english + history + geography

average = total / 5

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("Marksheet:")
print("----------")
print("Maths: ", maths)
print("Science: ", science)
print("English: ", english)
print("History: ", history)
print("Geography: ", geography)
print("----------")
print("Total: ", total)
print("Average: ", average)
print("Grade: ", grade)
