from django.shortcuts import render, redirect
import bcrypt
from .models import Cat, Dog, Cat_pic, Dog_pic
from django.core.urlresolvers import reverse

def index(request):
	context={
	'dogs': Dog.objects.filter(featured=True),
	'cats': Cat.objects.filter(featured=True)
	}
	return render(request, 'spca_app/index.html', context)

def cat_adoption(request):
	cats = Cat.objects.all()
	main_pics = Cat_pic.objects.filter(main = True)
	cat_pics = Cat_pic.objects.all()
	return render(request, 'spca_app/cat_adopt.html', context={'cats': cats, 'main_pics':main_pics, 'cat_pics':cat_pics})

def dog_adoption(request):
	dogs = Dog.objects.all()
	main_pics = Dog_pic.objects.filter(main = True)
	dog_pics = Dog_pic.objects.all()
	return render(request, 'spca_app/dog_adopt.html', context={'dogs': dogs, 'main_pics': main_pics, 'dog_pics':dog_pics})

def alumni(request):
	return render(request, 'spca_app/alumni.html')

def guardianangel(request):
	return render(request, 'spca_app/guardianangels.html')

def events(request):
	return render(request, 'spca_app/events.html')

def foster(request):
	return render(request, 'spca_app/foster.html')

def foster_cat(request):
	return render(request, 'spca_app/foster_cat.html')

def foster_cat_apply(request):
	return render(request, 'spca_app/cat_foster_app.html')

def foster_dog(request):
	return render(request, 'spca_app/foster_dog.html')

def volunteer(request):
	return render(request, 'spca_app/volunteer.html')

def donate(request):
	return render(request, 'spca_app/donate.html')

def contact(request):
	return render(request, 'spca_app/contact.html')

def partners(request):
	return render(request, 'spca_app/partners.html')

def newsletter(request):
	return render(request, 'spca_app/newsletter.html')

def health_behavior(request):
	return render(request, 'spca_app/health_behavior.html')

def health_behavior_canine(request):
	return render(request, 'spca_app/canine_health.html')

def health_behavior_feline(request):
	return render(request, 'spca_app/feline-health.html')

def lost_and_found(request):
	return render(request, 'spca_app/lost_and_found.html')

def admin(request):
	return render(request, 'spca_app/admin.html')

def admin_login(request):
	if request.method == 'POST':
		if request.POST['username'] == 'admin' and request.POST['password'] == 'password':
			request.session['admin'] = True
			return redirect('/admin/main')
		else:
			request.session['admin'] = False
			return redirect('/admin')

def admin_logout(request):
	request.session['admin'] = False
	return redirect('/admin')

def admin_main(request):
	if 'admin' not in request.session:
		return redirect('/admin')
	elif not request.session['admin']:
		return redirect('/admin')
	else:
		cats = Cat.objects.all().order_by('-featured', 'created_at')
		dogs = Dog.objects.all().order_by('-featured', 'created_at')
		return render(request, 'spca_app/admin_main.html', context={'cats':cats, 'dogs':dogs})

def add_dog(request):
	if not request.session['admin']:
		return redirect('/admin')
	else:
		return render(request, 'spca_app/add_dog.html')

def add_dog_submit(request):
	if request.method == 'POST':
		dog = Dog.objects.add(request.POST['name'],request.POST['status'],request.POST['breed'],request.POST['age'],request.POST['size'],request.POST['obedience'],request.POST['energy_level'],request.POST['with_dogs'],request.POST['with_kids'],request.POST['with_cats'],request.POST['comment_main'],request.POST['comment_bot'],request.POST['featured'],request.POST['special_need'])
		return redirect(reverse('spca:edit_dog',  kwargs={'id':dog.id}))

def edit_dog(request, id):
	dog = Dog.objects.get(id=id)
	dog_pics = Dog_pic.objects.filter(dog=dog)
	return render(request, 'spca_app/edit_dog.html', context={'dog':dog, 'dog_pics': dog_pics})

def edit_dog_submit(request):
	if request.method == 'POST':
		if 'featured' not in request.POST:
			featured = False
		else:
			featured = request.POST['featured']
		Dog.objects.update(request.POST['id'],request.POST['name'],request.POST['status'],request.POST['breed'],request.POST['age'],request.POST['size'],request.POST['obedience'],request.POST['energy_level'],request.POST['with_dogs'],request.POST['with_kids'],request.POST['with_cats'],request.POST['comment_main'],request.POST['comment_bot'],featured,request.POST['special_need'])
		dog_id = request.POST['id']
		return redirect('/admin/main')

def un_feature_dog(request, id):
	Dog.objects.un_feature(id)
	return redirect('/admin/main')

def delete_dog(request, id):
	Dog_pic.objects.delete_all(id)
	Dog.objects.delete(id)
	return redirect('/admin/main')

def add_dog_pics_submit(request):
	if request.method == 'POST':
		dog_id = request.POST['dog_id']
		Dog_pic.objects.add(dog_id, request.POST['url'])
		return redirect(reverse('spca:edit_dog',  kwargs={'id':dog_id}))

def delete_dog_pics(request, id):
	dog_id = Dog_pic.objects.get(id=id).dog.id
	Dog_pic.objects.delete(id)
	return redirect(reverse('spca:edit_dog',  kwargs={'id':dog_id}))

def add_cat(request):
	if not request.session['admin']:
		return redirect('/admin')
	else:
		return render(request, 'spca_app/add_cat.html')

def add_cat_submit(request):
	if request.method == 'POST':
		cat = Cat.objects.add(request.POST['name'],request.POST['born'],request.POST['status'],request.POST['sex'],request.POST['description'],request.POST['need_companion'],request.POST['with_dogs'],request.POST['with_kids'],request.POST['home_env'],request.POST['special_need'],request.POST['comment_main'],request.POST['comment_bot'],request.POST['featured'])
		return redirect(reverse('spca:edit_cat',  kwargs={'id':cat.id}))

def edit_cat(request, id):
	cat = Cat.objects.get(id=id)
	cat_pics = Cat_pic.objects.filter(cat=cat)
	return render(request, 'spca_app/edit_cat.html', context={'cat':cat, 'cat_pics': cat_pics})

def edit_cat_submit(request):
	if request.method == 'POST':
		if 'featured' not in request.POST:
			featured = False
		else:
			featured = request.POST['featured']
		if not request.POST['born']:
			print 'here'
			born = Cat.objects.get(id=request.POST['id']).born
		else:
			print 'there'
			born = request.POST['born']
		Cat.objects.update(request.POST['id'],request.POST['name'],born,request.POST['status'],request.POST['sex'],request.POST['description'],request.POST['need_companion'],request.POST['with_dogs'],request.POST['with_kids'],request.POST['home_env'],request.POST['special_need'],request.POST['comment_main'],request.POST['comment_bot'],featured)
		return redirect('/admin/main')

def un_feature_cat(request, id):
	Cat.objects.un_feature(id)
	return redirect('/admin/main')		

def delete_cat(request, id):
	Cat_pic.objects.delete_all(id)
	Cat.objects.delete(id)
	return redirect('/admin/main')

def add_cat_pics_submit(request):
	if request.method == 'POST':
		cat_id = request.POST['cat_id']
		Cat_pic.objects.add(cat_id, request.POST['url'])
		return redirect(reverse('spca:edit_cat',  kwargs={'id':cat_id}))

def delete_cat_pics(request, id):
	cat_id = Cat_pic.objects.get(id=id).cat.id
	Cat_pic.objects.delete(id)
	return redirect(reverse('spca:edit_cat',  kwargs={'id':cat_id}))