weight= float(input("What is your weight in kg? "))
height= float(input("What is your height in m?"))

height_squared = height * 2
bmi = round(weight / height_squared)
print(f"Your bmi number is {bmi}")

if bmi < 18.5: 
    print(f"You're under weight, your bmi is {bmi}")
elif bmi <= 24.9:
     print(f"You're normal weight, your bmi is {bmi}")
elif bmi <= 29.9:
    print(f"Overweight , your bmi is {bmi}")
elif bmi <= 34.9:
    print(f"You're class 1 Obese, , your bmi is {bmi}")
elif bmi <= 39.9:
    print (f"You're class 2 obese, your bmi is {bmi}")
else:
    print(f"Your bmi is {bmi} ,you need to lose weight, you're class 3 obese")