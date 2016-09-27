from django.shortcuts import render, redirect
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'spca_app/index.html')
