from django.db import models

class Food(models.Model):
	name = models.CharField(max_length=200)
	available = mopdels.BooleanField(default=False)
	date_added = models.DateTimeField()
	

class Food_Image(models.Model):
	name = models.ForeignKey(Food)
	image = models.URLField()
`
