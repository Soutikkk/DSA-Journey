marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: O")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 25:
    print("Grade: E")
elif marks >= 0:
    print("Remarks : ReExam")
else:
    print("Invalid marks entered.")