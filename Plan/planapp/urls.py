#from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from planapp import views
app_name = "planapp"  
 
 
urlpatterns = [

    path('',views.index),
    path('login/',views.user_login),
    path('register/',views.register),
    path('logout/', views.user_logout),
    path('admin_login/', views.admin_login),
    path('admin1/', views.admin1),
    path('edit_plan/<int:pk>/', views.edit_plan),
    path('del_plan/<int:pk>/', views.del_plan),
    path('add_plan/', views.add_plan),
    path('deposit/', views.deposit),
    path('update/<int:dk>/', views.update),
    path('accept/<int:dk>/', views.accept)


   
   
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
