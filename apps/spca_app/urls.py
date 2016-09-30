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
    url(r'^admin/delete_dog/(?P<id>\d+)$', views.delete_dog, name = "delete_dog"),
    url(r'^admin/edit_dog/(?P<id>\d+)$', views.edit_dog, name = "edit_dog"),
    url(r'^admin/edit_dog/submit$', views.edit_dog_submit, name = "edit_dog_submit"),
    url(r'^admin/un_feature_dog/(?P<id>\d+)$', views.un_feature_dog, name = "un_feature_dog"),
    url(r'^admin/add_dog_pic/submit$', views.add_dog_pics_submit, name = "add_dog_pics_submit"),
    url(r'^admin/delete_dog_pics/(?P<id>\d+)$', views.delete_dog_pics, name = "delete_dog_pics"),
    url(r'^admin/add_cat$', views.add_cat, name = "add_cat"),
    url(r'^admin/add_cat/submit$', views.add_cat_submit, name = "add_cat_submit"),
    url(r'^admin/delete_cat/(?P<id>\d+)$', views.delete_cat, name = "delete_cat"),
    url(r'^admin/edit_cat/(?P<id>\d+)$', views.edit_cat, name = "edit_cat"),
    url(r'^admin/edit_cat/submit$', views.edit_cat_submit, name = "edit_cat_submit"),
    url(r'^admin/un_feature_cat/(?P<id>\d+)$', views.un_feature_cat, name = "un_feature_cat"),
    url(r'^admin/add_cat_pic/submit$', views.add_cat_pics_submit, name = "add_cat_pics_submit"),
    url(r'^admin/delete_cat_pics/(?P<id>\d+)$', views.delete_cat_pics, name = "delete_cat_pics"),
]