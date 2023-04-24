weight=float(input("What is your weight? (in kg) "))
height=float(input("What is your height? (in m) "))

(BMI) = weight/height**2
if BMI <= 18.5:
  print(f"Your bmi is {BMI}, you are underweight")
if BMI >18.5 and BMI<=25:
  print(f"Your bmi is {BMI}, you have normal weight")
if BMI>25:
  print(f"Your bmi is {BMI}, you are overweight")
else:
  print("Wrong input")

