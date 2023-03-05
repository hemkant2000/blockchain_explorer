from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,), # our-domain.com/block_exp_app1
    path('block/', views.submit_form, name='submit-form'),
    path('trans/', views.submit_form1, name='submit-form1'),
]   