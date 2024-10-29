def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Display calculated BMI
    print("BMI = " + str(round(bmi, 2)))
    
    # Determine weight classification and return value
    if bmi < 18.5:
        return -1

    elif 18.5 <= bmi <= 25.0:
        return 0

    elif 25.0:
        return 1
    

result = calculate_bmi(weight=500, height=1.73)

if result==-1:
    print("Underweight")
elif result==0:
    print("Normal weight")
elif result==1:
    print("Overweight")
