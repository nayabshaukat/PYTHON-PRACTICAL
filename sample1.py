# 🟢 1. Store student data using a list of tuples (name and ID)
students = [("Ali", "S001"), ("Sara", "S002"), ("Hassan", "S003")]

# 🟡 2. Dictionary for scores (student ID → score)
scores = {
    "S001": 85,
    "S002": 72,
    "S003": 91
}

# 🟠 3. Function to calculate grade based on score
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    else:
        return "C"

# 🔵 4. Function to print the report
def print_report():
    print("---- Student Grades Report ----")
    for name, student_id in students:                      # looping over a list of tuples
        score = scores.get(student_id)                     # find score in dictionary
        grade = calculate_grade(score)                     # call a function
        print(f"{name} ({student_id}) → Score: {score}, Grade: {grade}")

# 🟣 5. Run the report function
print_report()