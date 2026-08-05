Height = float(input("Enter your height in cm: "))
Weight = float(input("Enter your weight in KG: "))

height = Height / 100
BMI = round(Weight / (height ** 2), 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI} and you are Underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI} and you have Normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI} and you are Overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI} and you are Obese.")
else:
    print(f"Your BMI is {BMI} and you are Clinically Obese.")