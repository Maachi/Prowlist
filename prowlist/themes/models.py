from django.db import models

#Referece for colors
class Color(models.Model):
	class Meta:
		verbose_name_plural = "Colors"

	name = models.CharField(max_length=200)
	red = models.DecimalField(max_digits=3, decimal_places=1)
	green = models.DecimalField(max_digits=3, decimal_places=1)
	blue = models.DecimalField(max_digits=3, decimal_places=1)


	def to_object(self):
		return {
			'name' : self.name
		}