'''Hospital'''

class Patient(object):
    def __init__(self, idNum, name, allergies, bedNum = None):
        self.idNum = idNum
        self.name = name
        self.allergies = allergies
        self.bedNum = bedNum
    
    def info(self):
        print "Patient Name: {}".format(self.name)
        print "ID number: {}".format(self.idNum)
        print "Allergies: {}".format(self.allergies)
        print "Bed Number: {}".format(self.bedNum)
        return self

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.patientCount = 0
    
    def admit(self, patient, bedNum):
        patient.bedNum = bedNum
        self.patientCount += 1
        if self.patientCount > self.capacity:
            self.patientCount -= 1
            print "Hospital is full"
        else: 
            self.patients.append(patient)
            print "Admission complete"
        return self
    
    def discharge(self, patient):
        patient.bedNum = None
        self.patients.remove(patient)
        self.patientCount -= 1
        return self

    def info(self):
        print "Hospital Name: {}".format(self.name)
        print "Capacity: {} / {}".format(self.patientCount, self.capacity)

        print "Patients:"
        for x in range(self.patientCount):
            print "ID: {}, Name: {}, Bed: {}, Allergies: {}".format(
                self.patients[x].idNum, 
                self.patients[x].name, 
                self.patients[x].bedNum,
                self.patients[x].allergies
                )
        return self

hospital1 = Hospital("Hospital1", 3)
patient1 = Patient(111, "Name 1", ['allergy1', 'allergy2', 'allergy3'])
patient2 = Patient(222, "Name 2", ['allergy1', 'allergy2', 'allergy3'])
hospital1.admit(patient1, 12).admit(patient2, 13).info().discharge(patient1).info()




