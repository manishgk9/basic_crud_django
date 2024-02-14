from django.urls import path
from core import views
urlpatterns = [
    path('', views.home, name='home_page'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>', views.edit_employee, name='edit_employee'),
    path('edit_help/<int:id>', views.edit_helper, name='edit_helper'),
    path('delete/<int:id>', views.delete_employee, name='delete_employee'),
]
