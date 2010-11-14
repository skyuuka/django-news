from django.db import models

# New Model (No pun intended)
class News(models.Model):
	title = models.TextField()
	body = models.TextField()
	url = models.TextField(blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	publish_date = models.DateTimeField()
	unpublish_date = models.DateTimeField()
