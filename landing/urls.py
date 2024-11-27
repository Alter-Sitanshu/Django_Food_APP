from django.urls import path

from .views import landing_view,detail_view,add_item,edit_item, delete_view

app_name = 'landing'
urlpatterns = [
    path('', landing_view, name='index'),
    path('<int:id>', detail_view, name='detail'),
    path('add', add_item, name='item_create'),
    path('edit/<int:id>', edit_item, name='item_edit'),
    path('delete/<int:id>', delete_view, name='delete'),
]