#build a hospital with patients in it.  create class Patients & Hospital


class Patient(object):
    count=1
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.count
        self.bed_num = None
        Patient.count += 1

class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(1, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bednum = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    print "Patient #"+str(patient.id)+ " admitted to bed #"+str(patient.bednum)
                else:
                    print "Hospital is at full capacity"
        return self 

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bednum:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #"+str(patient.id)+ " sucessfully discharged.  Bed #"+str(patient.bednum)+ "now available"
        return "Patient not found"


newPatient1 = Patient('Jane', 'nuts')
newPatient2 = Patient('John', 'shellfish')
newPatient3 = Patient('June', 'grass')
newPatient4 = Patient('Jeff', 'water')

hopkins = Hospital('John Hopkins', 3)   

hopkins.admit(newPatient1).admit(newPatient2).admit(newPatient3)