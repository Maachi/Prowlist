from themes.models import *
from django.db import models


class Tag(models.Model):
	class Meta:
		verbose_name_plural = "Tags"

	name = models.CharField(max_length=200)
	color = models.ForeignKey(Color)


	def __unicode__(self):
		return self.name