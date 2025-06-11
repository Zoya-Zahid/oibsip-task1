# bmi_calculator.py
# BMI Calculator using Python


def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight / (height * height)
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify the BMI into categories based on standard ranges.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_valid_input(prompt, min_value, max_value):
    """
    Get valid float input from the user between min_value and max_value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value or value > max_value:
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("========== BMI CALCULATOR ==========\n")

    # User input with validation
    weight = get_valid_input("Enter your weight in kilograms (30–200 kg): ", 30, 200)
    height = get_valid_input("Enter your height in meters (1.0–2.5 m): ", 1.0, 2.5)

    # BMI calculation and classification
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    # Output result
    print("\n========== RESULT ==========")
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category  : {category}")
    print("============================")

# Entry point
if __name__ == "__main__":
    main()
