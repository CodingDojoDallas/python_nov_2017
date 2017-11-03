#Assignment 7 Python OOP - Hospital
class patient(object):
	def __init__(self, uniqueID, name, allergies):
		self.uniqueID = uniqueID
		self.name = name
		self.allergies = allergies
		self.bedNumber = "none"

class hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []

	def admit(self, patient):
		if ((len(self.patients)+1) <= self.capacity):
			patient.bedNumber = 1
			self.patients.append(patient)
			print "The patient has been admited......:)"
		else:
			print "The Hospital is up to its max capacity....Patient Rejected.."

	def discharge(self, name):
		for i in range(0, len(self.patients)-1):
			if self.patients[i].name == name:
				self.patients[i].bedNumber = "none"
				self.patients.pop(i)

	def display(self):
		for i in self.patients:
			print i.name


patient1 = patient(1, "Rodolfo", "none")
patient2 = patient(2, "Mickey", "peanut")
patient3 = patient(3, "Thomas", "xxxxxx")
patient4 = patient(4, "Rick", "wwwwwww")
patient5 = patient(5, "Daniel", "aaaaaa")

hospital1 = hospital("The Dojo Hospital" , 3)

hospital1.admit(patient1)
hospital1.admit(patient2)
hospital1.admit(patient3)
hospital1.admit(patient4)
hospital1.admit(patient5)
hospital1.display()
print "Discharge Mickey..."
hospital1.discharge("Mickey")
hospital1.display()
