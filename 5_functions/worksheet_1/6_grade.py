def gradestudent(marks):
    if marks >= 90:
        print("A grade")
    elif marks >=80 and marks < 90:
        print("B grade")
    elif marks>=50 and marks < 80:
        print("C grade")
    else:
        print("D grade")


gradestudent(100)
gradestudent(50)
gradestudent(40)
gradestudent(75)