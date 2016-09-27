from django.shortcuts import render, redirect
import bcrypt
from .models import Cat, Dog, Cat_pic, Dog_pic
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'spca_app/index.html')

def cat_adoption(request):
	cats = Cat.objects.all()
	cat_pics = Cat_pic.objects.all()
	return render(request, 'spca_app/cat_adopt.html', context={'cats': cats, 'cat_pics':cat_pics})

def dog_adoption(request):
	dogs = Dog.objects.all()
	dog_pics = Dog_pic.objects.all()
	return render(request, 'spca_app/dog_adopt.html', context={'dogs': dogs, 'dog_pics':dog_pics})

def alumni(request):
	return render(request, 'spca_app/alumni.html')

def guardianangel(request):
	return render(request, 'spca_app/guardianangels.html')

def events(request):
	return render(request, 'spca_app/events.html')

def foster(request):
	return render(request, 'spca_app/foster.html')

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