from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<edit_item>/', views.edit_item, name='edits'),
    path('update/<update_item>', views.update, name='update'),
    path('delete/<delete_item>/', views.delet, name='delete'),
  
]