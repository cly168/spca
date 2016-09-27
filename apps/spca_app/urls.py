from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "my_index"),
    url(r'^adoption/catadoption$', views.cat_adoption, name = "cat_adoption"),
    url(r'^adoption/dogadoption$', views.dog_adoption, name = "dog_adoption"),
    url(r'^adoption/alumni$', views.alumni, name = "alumni"),
    url(r'^adoption/guardianangels$', views.guardianangel, name = "guardianangel"),
    url(r'^events$', views.events, name = "events"),
    url(r'^foster$', views.foster, name = "foster"),
    url(r'^help/volunteer$', views.volunteer, name = "volunteer"),
    url(r'^help/donate$', views.donate, name = "donate"),
    url(r'^about/contact$', views.contact, name = "contact"),
    url(r'^about/partners$', views.partners, name = "partners"),
    url(r'^about/newsletter$', views.newsletter, name = "newsletter"),
    url(r'^resources/health_behavior$', views.health_behavior, name = "health_behavior"),
    url(r'^resources/lost_and_found$', views.lost_and_found, name = "lost_and_found"),
]