percentage = float(input("Enter your percentage: "))
subject = input("Enter your subject(Math/Computer Science/Biology): ")

subject = subject.strip().lower()  # Remove any leading/trailing whitespace and convert to lowercase

if percentage >= 70 and (subject.lower() == "math" or subject.lower() == "computer science"):
    print("Eligible for admission to the college.")
    if percentage >= 90:
        print("Direct admission to the college.")
    else:
        if percentage >=80:
            if subject.lower() == "computer science":
                print("Priority admission to the college.")
            else:
                print("Application on hold for further review.")
        else:
            print("interview Call for admission to the college.")
else:
    print("Not eligible for admission to the college.")