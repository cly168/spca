from django.shortcuts import render, redirect
import bcrypt
from .models import Cat, Dog, Cat_pic, Dog_pic
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'spca_app/index.html')

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

def un_feature_dog(request, id):
	Dog.objects.un_feature(id)
	return redirect('/admin/main')

def delete_dog(request, id):
	Dog_pic.objects.delete_all(id)
	Dog.objects.delete(id)
	return redirect('/admin/main')

def edit_dog_submit(request):
	if request.method == 'POST':
		if 'featured' not in request.POST:
			featured = False
		else:
			featured = request.POST['featured']
		Dog.objects.update(request.POST['id'],request.POST['name'],request.POST['status'],request.POST['breed'],request.POST['age'],request.POST['size'],request.POST['obedience'],request.POST['energy_level'],request.POST['with_dogs'],request.POST['with_kids'],request.POST['with_cats'],request.POST['comment_main'],request.POST['comment_bot'],featured,request.POST['special_need'])
		dog_id = request.POST['id']
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