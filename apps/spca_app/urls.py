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
    url(r'^foster/cat$', views.foster_cat, name = "foster_cat"),
    url(r'^foster/dog$', views.foster_dog, name = "foster_dog"),
    url(r'^help/volunteer$', views.volunteer, name = "volunteer"),
    url(r'^help/donate$', views.donate, name = "donate"),
    url(r'^about/contact$', views.contact, name = "contact"),
    url(r'^about/partners$', views.partners, name = "partners"),
    url(r'^about/newsletter$', views.newsletter, name = "newsletter"),
    url(r'^resources/health_behavior$', views.health_behavior, name = "health_behavior"),
    url(r'^resources/lost_and_found$', views.lost_and_found, name = "lost_and_found"),
    url(r'^admin$', views.admin, name = "admin"),
    url(r'^admin/login$', views.admin_login, name = "admin_login"),
    url(r'^admin/logout$', views.admin_logout, name = "admin_logout"),
    url(r'^admin/main$', views.admin_main, name = "admin_main"),
    url(r'^admin/add_dog$', views.add_dog, name = "add_dog"),
    url(r'^admin/add_dog/submit$', views.add_dog_submit, name = "add_dog_submit"),
    url(r'^admin/add_dog/pics/(?P<id>\d+)$', views.add_dog_pics, name = "add_dog_pics"),
]