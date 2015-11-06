from themes.models import *
from django.db import models


class Tag(models.Model):
	class Meta:
		verbose_name_plural = "Tags"

	name = models.CharField(max_length=200)
	color = models.ForeignKey(Color)
	text_color = models.ForeignKey(Color, default=None, null=True, related_name='text_color')

	def __unicode__(self):
		return self.name

	def to_object(self):
		color = None
		text_color = None
		if self.color:
			color = self.color.to_object()
		if self.text_color:
			text_color = self.text_color.to_object()
		return {
			'name' : self.name,
			'color' : color,
			'text_color' : text_color,
		}