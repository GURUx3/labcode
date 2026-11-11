def diagnosis():
    print("MEDICAL DIAGNOSIS EXPERT SYSTEM")
    print("--------------------------------")

    fever = input("Do you have fever? (yes/no): ")
    cough = input("Do you have cough? (yes/no): ")
    headache = input("Do you have headache? (yes/no): ")
    sneezing = input("Do you have sneezing? (yes/no): ")
    bodypain = input("Do you have body pain? (yes/no): ")
    sorethroat = input("Do you have sore throat? (yes/no): ")

    if fever == "yes" and cough == "yes" and bodypain == "yes":
        disease = "Possible Flu"
        reason = "Fever, cough and body pain are present."
        treatment = "Take rest, drink fluids and consult a doctor."

    elif fever == "yes" and headache == "yes":
        disease = "Possible Viral Fever"
        reason = "Fever and headache are present."
        treatment = "Take rest, drink water and consult a doctor."

    elif sneezing == "yes" and cough == "yes":
        disease = "Possible Common Cold"
        reason = "Sneezing and cough are present."
        treatment = "Drink warm fluids and take adequate rest."

    elif cough == "yes" and sorethroat == "yes":
        disease = "Possible Throat Infection"
        reason = "Cough and sore throat are present."
        treatment = "Drink fluids and seek medical advice."

    else:
        disease = "Unknown Condition"
        reason = "Symptoms do not match the available rules."
        treatment = "Consult a doctor for proper diagnosis."

    print("\n----- DIAGNOSIS REPORT -----")
    print("Disease:", disease)
    print("Reason:", reason)
    print("Treatment:", treatment)


diagnosis()
