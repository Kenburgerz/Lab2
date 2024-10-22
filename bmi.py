def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    #Add code here to calculate bmi
    bmi = weight / (height ** 2)

    #Add code here to display calculate bmi
    print ("BMI =" + str(round(bmi, 2)))
    

    if bmi < 18.5:
        classification = "Under weight"
    elif 18.5 <= bmi <=25.0:
        classification = "Normal"

    else:
        classification = "Over weight"

    print("Weight classification = " + classification)
    return bmi

calculate_bmi(weight=57, height=1.73)

