# -------- PATIENT CLASS --------
class Patient:
    def __init__(self, name, age, symptoms):
        self.name = name
        self.age = age
        self.symptoms = symptoms
        self.diagnosis = None
        self.doctor = None
        self.medicine = None

    def display_info(self):
        print("\nPatient Name:", self.name)
        print("Age:", self.age)

        print("Symptoms:", end=" ")
        for s in self.symptoms:
            print(s, end=", ")

        print("\nDiagnosis:", self.diagnosis if self.diagnosis else "Pending")
        print("Assigned Doctor:", self.doctor if self.doctor else "Not Assigned")
        print("Suggested Medicine:", self.medicine if self.medicine else "Not Prescribed")


# -------- EXPERT SYSTEM --------
class HospitalExpertSystem:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        self.diagnose_patient(patient)

    def diagnose_patient(self, patient):
        fever = 0
        cough = 0
        fatigue = 0
        headache = 0
        stomach = 0

        # count symptoms
        for symptom in patient.symptoms:
            s = symptom.lower().strip()

            if "fever" in s:
                fever += 1
            if "cough" in s or "couph" in s:
                cough += 1
            if "fatigue" in s:
                fatigue += 1
            if "headache" in s:
                headache += 1
            if "stomach" in s:
                stomach += 1

        print("\nDebug - Symptom Counts:")
        print("Fever =", fever, 
              "Cough =", cough, 
              "Fatigue =", fatigue, 
              "Headache =", headache, 
              "Stomach =", stomach)

        # rules
        if fever > 0 and cough > 0 and fatigue > 0:
            patient.diagnosis = "Influenza (Flu)"
            patient.doctor = "Dr. Prasad Bire"
            patient.medicine = "Paracetamol, Cough Syrup"

        elif fever > 0 and headache > 0:
            patient.diagnosis = "Migraine or Viral Fever"
            patient.doctor = "Dr. Shruti Jadhav"
            patient.medicine = "Ibuprofen"

        elif stomach > 0 and fatigue > 0:
            patient.diagnosis = "Gastritis or Food Poisoning"
            patient.doctor = "Dr. Patel"
            patient.medicine = "Antacid, Fluids"

        elif cough > 0 and fatigue > 0:
            patient.diagnosis = "Common Cold"
            patient.doctor = "Dr. Singh"
            patient.medicine = "Rest, Cough Drops"

        elif fever > 0 and stomach > 0:
            patient.diagnosis = "Stomach Infection"
            patient.doctor = "Dr. Patel"
            patient.medicine = "Antacid, Paracetamol"

        elif cough > 0:
            patient.diagnosis = "Mild Cough"
            patient.doctor = "Dr. Singh"
            patient.medicine = "Cough Drops"

        else:
            patient.diagnosis = "Consult Specialist"
            patient.doctor = "Not Assigned"
            patient.medicine = "Not Prescribed"

    def display_all(self):
        if len(self.patients) == 0:
            print("No patients in system")
            return

        print("\n--- All Patients ---")
        for p in self.patients:
            p.display_info()


# -------- MAIN --------
hospital = HospitalExpertSystem()

print("Welcome to Hospital Expert System")

while True:
    print("\n1. Add Patient")
    print("2. Display Patients")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        symptom_input = input("Enter symptoms (comma separated): ")

        symptoms = symptom_input.split(",")

        patient = Patient(name, age, symptoms)
        hospital.add_patient(patient)

        print("\nPatient Added Successfully!")
        patient.display_info()

    elif choice == 2:
        hospital.display_all()

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice")