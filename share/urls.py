from django.contrib import admin  # Import the admin module
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('explore/', views.explore, name='explore'),
    path('book_image/', views.book_image, name='book_image'),
    path('success/', views.success, name='success'),
    path('contact/', views.contact, name='contact'),
    path('insert/', views.create_view, name='insert'),
    path('more/', views.book_view, name='book_view'),
    path('delete_material/<int:id>/', views.delete_material, name='delete_material'),
    path('update_material/<int:id>/', views.update_material, name='update_material'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
