from django.db import models

#Referece for colors
class Color(models.Model):
	class Meta:
		verbose_name_plural = "Colors"

	name = models.CharField(max_length=200)
	red = models.IntegerField()
	green = models.IntegerField()
	blue = models.IntegerField()
	alpha = models.IntegerField()


	def __unicode__(self):
		return self.name


	def to_object(self):
		return {
			'name' : self.name
		}