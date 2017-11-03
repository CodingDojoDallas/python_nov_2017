class Patient(object):
	unique_id = 0
	def __init__(self, name, allergies):
		patient.unique_id +=1
		self.idn = patient.unique_id
		self.name = name
		self.allergies = allergies
		self.bednum = none
	def info(self):
		print "Name: {}, ID: {}, Allergies: {} Bed Number: {}".format(self.name, self.idn, self.allergies, self.bednum)

pat1 = Patient('Jimmy', 'Peanuts')	
pat2 = Patient(2, 'Slim', 'None', 'none')




class Hospital(Patient):
	def __init__(self, patients, Hname, cap):
		self.patients = []
		self.Hname = Hname
		self.cap = cap
		self.beds = 

	


