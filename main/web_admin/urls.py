from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('product/', views.product_view, name='product'),
    path('videos/', views.video_view, name='videos'),
]
