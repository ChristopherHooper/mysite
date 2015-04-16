import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1)<=self.pub_date<=now
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Category(models.Model):
	CId = models.CharField(max_length = 200)
	short_name = models.CharField(max_length = 200)
	def __str__(self):
		return self.short_name

class Eve(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=2000)
	description = models.CharField(max_length=2000)
	def __str__(self):
		return self.name

class Events(models.Model):
	first = models.CharField(default="?", max_length = 2000)
	second = models.CharField(default="?", max_length = 2000)
	third = models.CharField(default="?", max_length = 2000)

	