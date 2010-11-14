from django.db import models

# New Model (No pun intended)
class News(models.Model):
	title = models.TextField(blank=True)
	body = models.TextField()
	#url = models.TextField(blank=True)
	publish_date = models.DateTimeField(blank=True, null=True)
	unpublish_date = models.DateTimeField(blank=True, null=True)
	order = models.IntegerField(unique=True)
	create_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)