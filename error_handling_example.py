# loan eligibility checker

try:
    income = float(input("Enter your annual income(INR): "))
    age = int(input("Enter your age: "))
    loan_amount = float(input("Enter the loan amount requested(INR): "))
    loan_term = int(input("Enter the loan term (in years): "))
    credit_score = int(input("Enter your credit score(300-900): "))

    if income <=0 or loan_amount <=0 or loan_term <=0:
        print("Income, loan amount, and loan term must be greater than zero.")
    elif credit_score < 300 or credit_score > 900:
        print("Credit score must be between 300 and 900.")
    else:
        if age < 21 or age > 60:
            print("Loan Status: Rejected ")
            print("Reason: Age must be between 21 and 60 years.")
        else:
            #EMI Calculation
            P = loan_amount
            r = 0.1 / 12  # Assuming a fixed annual interest rate of 10%
            n = loan_term * 12  # Convert years to months


            EMI = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
            EMI = round(EMI, 2)

            if credit_score >= 750:
                credit_rating = "Excellent"
            elif credit_score >= 650:   
                credit_rating = "Good"
            else:
                credit_rating = "Average"
            
            print(f"EMI: INR {EMI}")
            print(f"Credit Rating: {credit_rating}")

            if(credit_rating == "Average"):
                print("Loan Status: Rejected")
                print("Reason: Credit score is below the acceptable threshold.")
            elif EMI > (income * 0.4):
                print("Loan Status: Eligible")
                print("Reason: EMI exceeds 40% of your income.")
            else:
                print("Loan Status: Rejected")
                print("Reason: EMI exceeds 40% of your income.")

except ValueError:
    print("Invalid input. Please enter numeric values for income, age, loan amount, loan term, and credit score.")

except ZeroDivisionError:
    print("Loan term cannot be zero. Please enter a valid loan term.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")