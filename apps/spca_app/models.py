from django.db import models

# Create your models here.
class Cat(models.Model):
	name = models.CharField(max_length=255)
	born = models.DateField(auto_now=False)
	status = models.CharField(max_length=45)
	sex = models.CharField(max_length=45)
	description = models.CharField(max_length=45)
	need_companion = models.CharField(max_length=255)
	with_dogs = models.CharField(max_length=45)
	with_kids = models.CharField(max_length=45)
	home_env = models.CharField(max_length=45)
	special_need = models.CharField(max_length=255)
	comment_main = models.TextField()
	comment_bot = models.CharField(max_length=255)
	featured = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Cat_pic(models.Model):
	cat = models.ForeignKey(Cat, related_name='picturetocat')
	url = models.CharField(max_length=255)
	main = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Dog(models.Model):
	name = models.CharField(max_length=255)
	status = models.CharField(max_length=45)
	breed = models.CharField(max_length=255)
	age = models.CharField(max_length=45)
	size = models.CharField(max_length=45)
	obedience = models.CharField(max_length=45)
	energy_level = models.CharField(max_length=45)
	with_dogs = models.CharField(max_length=45)
	with_kids = models.CharField(max_length=45)
	with_cats = models.CharField(max_length=45)
	comment_main = models.TextField()
	comment_bot = models.CharField(max_length=255)
	featured = models.BooleanField(default=False)
	special_need = models.CharField(max_length=255, default='')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Dog_pic(models.Model):
	dog = models.ForeignKey(Dog, related_name='picturetodog')
	url = models.CharField(max_length=255)
	main = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)