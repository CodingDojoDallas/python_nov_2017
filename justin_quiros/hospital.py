from datetime import datetime

class Patient(object):
	uniqid = 1
	def __init__(self, name, allergies):
		self.idnum = Patient.uniqid
		self.name = name
		self.allergies = allergies
		self.bed = None

		Patient.uniqid += 1

	def patient_info(self):
		print self.idnum
		print self.name
		print self.allergies
		print self.bed
		return self


class Hospital(object):
	patients = []

	def __init__(self, name, capacity):
		self.name = name
		self.patients = []
		self.capacity = capacity
		self.bed_assign = self.bed_assignment()

	def bed_assignment(self):
		beds = []
		for x in range(0, self.capacity):
			beds.append({
				"bed_id": x,
				"Available": True
				})
			return beds

	def admit(self, patient):
		if len(self.patients) <= self.capacity:
			self.patients.append(patient)
			for x in range(0, len(self.bed_assign)):
				if self.bed_assign[x]["Available"]:
					patient.bed = self.bed_assign[x]["bed_id"]
					self.bed_assign[x]["Available"] = False
				break
			print "Patient #{} admitted to bed #{}".format(patient.idnum, patient.bed)
		else:
			"Sorry, we are currently full"

	def discharge(self, discharge_pat):
		for patient in self.patients:
			if patient.idnum == discharge_pat.idnum:
				for bed in self.bed_assign:
					if bed["bed_id"] == patient.bed:
						bed["Available"] = True
						break
				self.patients.remove(patient)
				return "Patient #{} successfully discharged. Bed #{} now available.".format(patient.idnum, patient.bed)
			return "We cannot find that patient"
	# def info(self):
	# 	for x in self.patients:
	# 		x.patient_info()

patient1 = Patient("Justin", "Peanuts, Cats")
patient2 = Patient("John", "Dogs, Dairy")
patient3 = Patient("Sally", "Chocolate, Peanuts")

hospital1 = Hospital("Saint Jude's", 5)

hospital1.admit(patient1)
hospital1.admit(patient2)
hospital1.admit(patient3)
ihospital1.discharge(patient1)








