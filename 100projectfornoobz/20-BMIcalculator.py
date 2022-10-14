

height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

bmi = weight/(height/100)**2
print(bmi)
if bmi <= 18:
    print("No cap! You are a broke ass nigga. Eat some bread you mf.")
elif bmi < 25:
    print("I never lie about fitness. You have 10/10 physique.")
elif bmi < 30:
    print("No cap, you have some extra weight. you need to give a few kilograms.")
elif bmi >= 30:
    print("You fat nigga, get that big ass up and do some sports. You loser.")
