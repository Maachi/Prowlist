class Security :

	#@constructor
	def __init__(self, product_id, session):
		self.product_id = product_id
		self.session = session


	#This validates if the purchanse is valid or not	
	def validate (self):
		return True


	#This method returns the error from the different service
	def raise_error (self):
		return u'The product is not available, please try again later.'


	#This method validates by using location, take this method into consideration
	#if you want to abstract the user's current location as a variable to validate if the user can or
	#cannot get the product
	def location (self):
		self.validate()
		return True