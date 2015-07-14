from themes.models import *
from django.db import models


class Tag(models.Model):
	class Meta:
		verbose_name_plural = "Tags"

	name = models.CharField(max_length=200)
	color = models.ForeignKey(Color)


	def __unicode__(self):
		return self.name

	def to_object(self):
		color = None
		if self.color:
			color = self.color.to_object()
		return {
			'name' : self.name,
			'color' : color,
		}