from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('contacts/edit/<int:pk>/', views.update_contact, name='update_contact'),
    path('contacts/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('categories/', views.category_list, name='category_list'),
]
