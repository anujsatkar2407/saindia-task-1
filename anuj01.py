def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {bmi_category(bmi)}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()