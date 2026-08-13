def get_user_float(prompt,min_value=0.0):
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            print(f"Please enter value >{min_value}.")
        except ValueError:
            print("That's wasn't a valid number")

def calculate_bmi(weight_kg,height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("== BMI & Calorie Needs Helper ==")
    weight = get_user_float("Enter your weight (kg): ",1)
    heigth = get_user_float("Enter your height (cm): ",30) / 100

    bmi = calculate_bmi(weight,heigth)
    category = bmi_category(bmi)

    print(f"\nYour BMI is {bmi:.1f} - {category}")
    print("\nThanks for using BMI Calculator")

main()