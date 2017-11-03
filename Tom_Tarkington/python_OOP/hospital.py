global idcounter
idcounter = 1000

class Patient(object):

    def __init__(self, name, allergies=["None"], bed_number="none", id=0,):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
    
class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.open_beds = []
        for idx in range (1, self.capacity+1):
            self.open_beds.append(idx)
    
    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Sorry we can't admit any more patients because the hospital is full."
        else:
            global idcounter
            idcounter += 1
            patient.id = idcounter
            self.patients.append(patient)
            patient.bed_number = self.open_beds.pop(0)
            print patient.name + " has been assigned bed #", str(patient.bed_number)
        return self

    def discharge(self, patient):
        if patient in self.patients:
            self.open_beds.append(patient.bed_number)
            patient.bed_number = "None"
            self.patients.remove(patient)
            print ""
            print "Patient {} has been discharged.".format(patient.name)
        else:
            print "* * * * * * * * * * * * * * * * * * * * * * * * * * * *"
            print "We can't discharge a patient who isn't in the hospital!"
            print "* * * * * * * * * * * * * * * * * * * * * * * * * * * *"
        return self
    
    def display_info(self):
        print ""
        print "There are currently {} patients at {}".format(str(len(self.patients)), self.name) 
        for search in self.patients:
            print ""
            print "Patient ID:", str(search.id)
            print "Bed #:", str(search.bed_number)
            print "Name:", search.name
            print "Allergies:", search.allergies
        return self

Tom = Patient("Tom")
Larry = Patient("Larry", "Mellon")
Kathy = Patient("Kathy", "Pollen")
Lynn = Patient("Lynn", "Lactose Intollerant")
Ed = Patient("Ed", "Peanuts")

hospital = Hospital("Plano Medical Center", 3)

hospital.admit(Tom).admit(Larry).admit(Kathy).admit(Lynn).display_info()
hospital.discharge(Larry).display_info()
hospital.discharge(Larry).admit(Lynn).display_info()
