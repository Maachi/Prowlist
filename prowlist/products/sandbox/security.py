class Security :

	#@constructor
	def __init__(self, location, session):
		self.location = location
		self.session = session


	def validate (self):
		return True

	#This method validates by using location, take this method into consideration
	#if you want to abstract the user's current location as a variable to validate if the user can or
	#cannot get the product
	def location (self):
		self.validate()
		return True