from django.db import models

# Create your models here.
class DogManager(models.Manager):
	def add(self, name, status, breed, age, size, obedience, energy_level, with_dogs, with_kids, with_cats, comment_main, comment_bot, featured, special_need):
		Dog.objects.create(name=name, status=status, breed=breed, age=age, size=size, obedience=obedience, energy_level=energy_level, with_dogs=with_dogs, with_kids=with_kids, with_cats=with_cats, comment_main=comment_main, comment_bot=comment_bot, featured=featured, special_need=special_need)
		return Dog.objects.latest('id')
	def update(self, id, name, status, breed, age, size, obedience, energy_level, with_dogs, with_kids, with_cats, comment_main, comment_bot, featured, special_need):
		dog = Dog.objects.get(id=id)
		dog.name = name
		dog.status = status
		dog.breed = breed
		dog.age = age
		dog.size = size
		dog.obedience = obedience
		dog.energy_level = energy_level
		dog.with_dogs = with_dogs
		dog.with_kids = with_kids
		dog.with_cats = with_cats
		dog.comment_main = comment_main
		dog.comment_bot = comment_bot
		dog.featured = featured
		dog.special_need = special_need
		dog.save()
	def un_feature(self, id):
		dog = Dog.objects.get(id=id)
		if dog.featured:
			dog.featured = False
		else:
			dog.featured = True
		dog.save()
	def delete(self, id):
		Dog.objects.get(id=id).delete()

class Dog_picManager(models.Manager):
	def add(self, id, url):
		dog = Dog.objects.get(id=id)
		if Dog_pic.objects.filter(dog=dog).filter(main=True):
			Dog_pic.objects.create(dog=dog, url=url)
		else:
			Dog_pic.objects.create(dog=dog, url=url, main=True)
	def delete(self, id):
		Dog_pic.objects.get(id=id).delete()
	def delete_all(self, id):
		dog = Dog.objects.get(id=id)
		pics = Dog_pic.objects.filter(dog=dog)
		for pic in pics:
			Dog_pic.objects.get(id=pic.id).delete()

class CatManager(models.Manager):
	def add(self,name,born,status,sex,description,need_companion,with_dogs,with_kids,home_env,special_need,comment_main,comment_bot,featured):
		Cat.objects.create(name=name,born=born,status=status,sex=sex,description=description,need_companion=need_companion,with_dogs=with_dogs,with_kids=with_kids,home_env=home_env,special_need=special_need,comment_main=comment_main,comment_bot=comment_bot,featured=featured)
		return Cat.objects.latest('id')
	def update(self,id,name,born,status,sex,description,need_companion,with_dogs,with_kids,home_env,special_need,comment_main,comment_bot,featured):
		cat = Cat.objects.get(id=id)
		cat.name = name
		cat.born = born
		cat.status = status
		cat.sex = sex
		cat.description = description
		cat.need_companion = need_companion
		cat.with_dogs = with_dogs
		cat.with_kids = with_kids
		cat.home_env = home_env
		cat.special_need = special_need
		cat.comment_main = comment_main
		cat.comment_bot = comment_bot
		cat.featured = featured
		cat.save()
	def un_feature(self, id):
		cat = Cat.objects.get(id=id)
		if cat.featured:
			cat.featured = False
		else:
			cat.featured = True
		cat.save()
	def delete(self, id):
		Cat.objects.get(id=id).delete()

class Cat_picManager(models.Manager):
	def add(self, id, url):
		cat = Cat.objects.get(id=id)
		if Cat_pic.objects.filter(cat=cat).filter(main=True):
			Cat_pic.objects.create(cat=cat, url=url)
		else:
			Cat_pic.objects.create(cat=cat, url=url, main=True)
	def delete(self, id):
		Cat_pic.objects.get(id=id).delete()
	def delete_all(self, id):
		cat = Cat.objects.get(id=id)
		pics = Cat_pic.objects.filter(cat=cat)
		for pic in pics:
			Cat_pic.objects.get(id=pic.id).delete()

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
	objects = CatManager()

class Cat_pic(models.Model):
	cat = models.ForeignKey(Cat, related_name='picturetocat')
	url = models.CharField(max_length=255)
	main = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Cat_picManager()

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
	objects = DogManager()

class Dog_pic(models.Model):
	dog = models.ForeignKey(Dog, related_name='picturetodog')
	url = models.CharField(max_length=255)
	main = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = Dog_picManager()