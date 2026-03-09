students = {
    "Rahul": 85,
    "Amit": 90,
    "Neha": 78,
    "Priya": 95
}

topper = max(students, key=students.get)

print("Topper:", topper)
print("Marks:", students[topper])
