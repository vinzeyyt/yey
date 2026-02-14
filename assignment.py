def clr():
    print("\n" * 67)

def checker(grade):
    while True:
        try:
            gradelol = int(input(grade))
            if (gradelol) < 10 or (gradelol) > 100:
                clr()
                print("\rOnly grades between 10 and 100 are allowed. Please try again.")
            else:
                return gradelol
        except ValueError:
            clr()
            print("Please enter a valid grade: ")

name = (input("Enter your name: "))

clr()
fprelim = checker("Enter your first semester prelim grade: ")
clr()
fmidterm = checker("Enter your first semester midterm grade: ")
clr()
ffinals = checker("Enter your first semester finals grade: ")
clr()
sprelim = checker("Enter your second semester prelim grade: ")
clr()
smidterm = checker("Enter your second semester midterm grade: ")
clr()
sfinals = checker("Enter your second semester finals grade: ")

fsemavg = (fprelim + fmidterm + ffinals) / 3
ssemavg = (sprelim + smidterm + sfinals) / 3
fwa = (fsemavg + ssemavg) / 2

clr()
print(f"\nStudent Name: {name}")
print(f"\nFirst Semester Average: {int(fsemavg)}")
print(f"Second Semester Average: {int(ssemavg)}")
print(f"Final Weighted Average: {int(fwa)}")

if fwa >= 75:
    print("\nRemarks: Passed")
else:
    print("\nRemarks: You are a LOSER")